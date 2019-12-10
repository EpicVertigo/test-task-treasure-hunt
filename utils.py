"""
Utility functions for both implementations
"""
import json


class BoardValidationError(BaseException):
    pass


def get_digit(number: int, n: int) -> int:
    """Returns specific nth digit. Indexing from right to left starts at 0"""
    return number // 10**n % 10


def validate_board(board_data: list) -> bool:
    """
    Checks if size of two-dimentional array is 5x5
    This also could be done by converting incoming data into Numpy 
    array and check it's shape
    """
    rows_lengths = {len(x) for x in board_data}
    if len(board_data) == 5 and len(rows_lengths) == 1 and list(rows_lengths)[0] == 5:
        return True
    raise BoardValidationError('Board must be 5 x 5')


def read_json_board(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        board_data = json.load(f)
    if validate_board(board_data):
        return board_data
