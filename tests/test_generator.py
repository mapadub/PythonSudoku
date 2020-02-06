import pytest
from unittest import mock
from generator import Generator


@pytest.fixture
def generator():
    return Generator()


def test_generate_grid(generator):
    #TODO is valid and solvale
    pass


def grid_is_valid(grid):
    # check all rows
    # check columns
    # check boxes
    return False

