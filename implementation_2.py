from utils import get_digit, read_json_board


def board_solver(board: list):
    moves = []
    solved = False

    def move_to_next_cell(x: int = 1, y: int = 1) -> list:
        nonlocal solved
        if solved:
            solved = False
            moves.clear()
        current_cell = int(f'{x}{y}')
        moves.append(current_cell)
        next_cell = board[x - 1][y - 1]
        if next_cell == current_cell:
            solved = True
            return moves
        next_x, next_y = get_digit(next_cell, 1), get_digit(next_cell, 0)
        return move_to_next_cell(next_x, next_y)

    return move_to_next_cell


if __name__ == "__main__":
    board_data = read_json_board('treasure_map.json')
    solver = board_solver(board_data)
    try:
        result = solver(1, 1)
        print(f'Output path is: {", ".join([str(x) for x in result])}')
    except RecursionError as exc:
        print(f'This board can not be solved using {exc.args[0]} as first step')
