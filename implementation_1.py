from typing import List, Union

from utils import get_digit, read_json_board


class CellNotFoundError(BaseException):
    pass


class Cell:
    """Represents cell on treasure map board

    Attributes:
        x: X coordinate on board
        y: Y coordinate on board
        clue: Content of the cell with clue for next step
    """
    __slots__ = 'x', 'y', 'clue'

    def __init__(self, x: int, y: int, clue: Union[int, str]):
        self.x, self.y = x, y
        self.clue = clue

    @property
    def is_treasure_cell(self) -> bool:
        return self.coordinates == self.clue_coordinates

    @property
    def coordinates(self) -> tuple:
        return self.x, self.y

    @property
    def clue_coordinates(self) -> tuple:
        if isinstance(self.clue, str) and len(self.clue) == 2:
            return int(self.clue[0]), int(self.clue[1])
        return get_digit(self.clue, 1), get_digit(self.clue, 0)

    def __repr__(self):
        return f'Cell:{self.coordinates} Clue:{self.clue_coordinates}'


class Board:
    """
    Represents board object that holds the list of all cells on map
    """
    __slots__ = 'cells'

    def __init__(self, board_data: list):
        self.cells = self._generate_board(board_data)

    def _generate_board(self, board_data: list) -> List[Cell]:
        """Converts board data to list of `Cell` objects"""
        cells = []
        for row_index, row in enumerate(board_data, 1):
            cells.extend([
                Cell(x=row_index, y=column_index, clue=clue)
                for column_index, clue in enumerate(row, 1)
            ])
        return cells

    def get_cell(self, x: int, y: int) -> Cell:
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        else:
            raise CellNotFoundError(f'No such cell with coordinates ({x}, {y})')


class TreasureHuntSolver:
    """Solver object 

    Attributes:
        board: instance of Board class
        moves: list of all moves required to reach the goal
        solved: flag that indicates if solver object solved current board
        traveled_cells: set of Cell objects used to detect if board is unsolvable
    """

    def __init__(self, board: Board):
        self.board = board
        self.moves = []
        self.solved = False
        self.traveled_cells = set()

    def print_result(self):
        if self.solved:
            print(f'Treasure hunt solved!\n'
                  f'Output path is: {", ".join([str(x) for x in self.moves])}')
        else:
            print('Current board is not solved yet')

    def reset_solver(self):
        """Resets current instance attributes for reusability"""
        self.traveled_cells.clear()
        self.moves.clear()
        self.solved = False

    def solve(self, x: int = 1, y: int = 1):  # Default first step is 1, 1
        if self.solved:
            self.reset_solver()
        self.moves.append(int(f'{x}{y}'))
        active_cell = self.board.get_cell(x, y)
        while not self.solved:
            if active_cell in self.traveled_cells:
                # By definition we can't travel thought same cell twice
                print(f'This board can not be solved using this first step ({x}, {y})')
                break
            if active_cell.is_treasure_cell:
                self.solved = True
                self.print_result()
                break
            self.moves.append(active_cell.clue)
            self.traveled_cells.add(active_cell)
            active_cell = self.board.get_cell(*active_cell.clue_coordinates)
        return self.moves if self.solved else None


if __name__ == "__main__":
    board_data = read_json_board('treasure_map.json')
    board = Board(board_data)
    result = TreasureHuntSolver(board).solve()
