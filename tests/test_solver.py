import pytest
import numpy as np
from Solver import Solver
from grid_wrapper import GridWrapper


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def solvable_sudoku():
    array = np.array([[0, 2, 0, 6, 0, 0, 0, 0, 5],
                     [5, 4, 9, 0, 3, 0, 8, 1, 0],
                     [0, 0, 0, 0, 8, 5, 7, 0, 0],
                     [0, 8, 0, 0, 4, 7, 9, 0, 0],
                     [0, 0, 7, 2, 1, 0, 0, 3, 0],
                     [6, 3, 0, 0, 0, 0, 0, 7, 4],
                     [0, 7, 1, 8, 6, 9, 4, 5, 3],
                     [9, 0, 0, 5, 0, 0, 0, 8, 0],
                     [0, 0, 3, 0, 2, 4, 0, 0, 0]])
    return GridWrapper(array)


@pytest.fixture
def not_solvable_sudoku():
    array = np.array([[0, 1, 0, 6, 0, 0, 0, 0, 5],
                     [5, 4, 9, 0, 3, 0, 8, 1, 0],
                     [0, 0, 0, 0, 8, 5, 7, 0, 0],
                     [0, 8, 0, 0, 4, 7, 9, 0, 0],
                     [0, 0, 7, 2, 1, 0, 0, 3, 0],
                     [6, 3, 0, 0, 0, 0, 0, 7, 4],
                     [0, 7, 1, 8, 6, 9, 4, 5, 3],
                     [9, 0, 0, 5, 0, 0, 0, 8, 0],
                     [0, 0, 3, 0, 2, 4, 0, 0, 0]])
    return GridWrapper(array)


def test_solvable(solver, solvable_sudoku):
    assert solver.is_solvable(solvable_sudoku)


def test_not_solvable(solver, not_solvable_sudoku):
    assert not solver.is_solvable(not_solvable_sudoku)
