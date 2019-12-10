from os.path import join

import pytest

from tests.fixtures import BOARDS_PATH, correct_board
from utils import (BoardValidationError, get_digit, read_json_board,
                   validate_board)


def test_get_ndigit():
    number = 15
    assert get_digit(number, 1) == 1
    assert get_digit(number, 0) == 5


def test_board_validation(correct_board):
    incorrect_width_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1], [2]]
    incorrect_height_board = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    with pytest.raises(BoardValidationError) as exception:
        validate_board(incorrect_width_board)
    with pytest.raises(BoardValidationError) as exception:
        validate_board(incorrect_height_board)
    assert validate_board(correct_board)


def test_read_json_board(correct_board):
    filename = join(BOARDS_PATH, 'correct_board.json')
    data = read_json_board(filename)
    assert data == correct_board
