import pytest
import numpy as np
from Solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def solvable_sudoku():
    grid = np.array([[0, 2, 0, 6, 0, 0, 0, 0, 5],
                     [5, 4, 9, 0, 3, 0, 8, 1, 0],
                     [0, 0, 0, 0, 8, 5, 7, 0, 0],
                     [0, 8, 0, 0, 4, 7, 9, 0, 0],
                     [0, 0, 7, 2, 1, 0, 0, 3, 0],
                     [6, 3, 0, 0, 0, 0, 0, 7, 4],
                     [0, 7, 1, 8, 6, 9, 4, 5, 3],
                     [9, 0, 0, 5, 0, 0, 0, 8, 0],
                     [0, 0, 3, 0, 2, 4, 0, 0, 0]])
    return grid


@pytest.fixture
def not_solvable_sudoku():
    grid = np.array([[0, 2, 0, 6, 0, 0, 0, 0, 5],
                     [5, 4, 9, 0, 3, 0, 8, 1, 0],
                     [0, 0, 0, 0, 8, 5, 7, 0, 0],
                     [0, 8, 0, 0, 4, 7, 9, 0, 0],
                     [0, 0, 7, 2, 1, 0, 0, 3, 0],
                     [6, 3, 0, 0, 0, 0, 0, 7, 4],
                     [0, 7, 1, 8, 6, 9, 4, 5, 3],
                     [9, 0, 0, 5, 0, 0, 0, 8, 0],
                     [0, 0, 3, 0, 2, 4, 0, 0, 0]])
    return grid


def test_grid_is_none(solver):
    with pytest.raises(TypeError):
        solver.solveble()


def test_solvable(solver, solvable_sudoku):
    solver.set_grid(solvable_sudoku)
    assert not solver.solveble()


def test_not_solvable(solver, not_solvable_sudoku):
    solver.set_grid(not_solvable_sudoku)
    assert not solver.solveble()
