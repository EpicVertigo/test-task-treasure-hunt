import json
from os.path import join

import pytest

BOARDS_PATH = join('tests', 'boards')


@pytest.fixture
def correct_board():
    with open(join(BOARDS_PATH, 'correct_board.json'), 'r') as f:
        return json.load(f)


@pytest.fixture
def incorrect_board():
    """Board that can not be solved by starting at (1, 1)"""
    with open(join(BOARDS_PATH, 'incorrect_board.json'), 'r') as f:
        return json.load(f)
