import pytest
import numpy as np
from grid_wrapper import GridWrapper


@pytest.fixture
def wrong_shaped_grid():
    return np.zeros((4, 5))


def test_grid_is_none():
    with pytest.raises(TypeError):
        GridWrapper(None)


def test_grid_is_wrong_shape(wrong_shaped_grid):
    with pytest.raises(ValueError):
        GridWrapper(wrong_shaped_grid)
