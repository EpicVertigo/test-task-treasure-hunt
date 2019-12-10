
import pytest


from implementation_2 import board_solver
from tests.fixtures import correct_board, incorrect_board


def test_solving_correct_board(correct_board):
    solver = board_solver(correct_board)
    assert solver() == [
        11, 34, 42, 15, 25, 31, 54, 13, 32, 45, 35, 23, 43, 51, 21, 14, 41, 33, 52]


def test_solving_incorrect_board(incorrect_board):
    solver = board_solver(incorrect_board)
    with pytest.raises(RecursionError) as exc_info:
        solver()


def test_reusability(correct_board):
    solver = board_solver(correct_board)
    assert solver(1, 1) == [11, 34, 42, 15, 25, 31, 54, 13, 32,
                            45, 35, 23, 43, 51, 21, 14, 41, 33, 52]
    # Same solver should be reusable with different starting point
    assert solver(2, 2) == [22, 42, 15, 25, 31, 54, 13, 32,
                            45, 35, 23, 43, 51, 21, 14, 41, 33, 52]
