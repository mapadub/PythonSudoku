import pytest
import numpy as np
import Solver


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
    grid = np.array([[0, 1, 0, 6, 0, 0, 0, 0, 5],
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
def wrong_shaped_grid():
    return np.zeros((4, 5))


@pytest.fixture
def full_grid():
    return np.full((9, 9), 1, dtype=int)


def test_grid_is_none():
    with pytest.raises(TypeError):
        Solver.solvable(None)


def test_grid_is_wrong_shape(wrong_shaped_grid):
    with pytest.raises(TypeError):
        Solver.solvable(wrong_shaped_grid)


def test_grid_is_already_filled(full_grid):
    with pytest.raises(ValueError):
        Solver.solvable(full_grid)


def test_solvable(solvable_sudoku):
    assert Solver.solvable(solvable_sudoku)


def test_not_solvable(not_solvable_sudoku):
    assert not Solver.solvable(not_solvable_sudoku)
