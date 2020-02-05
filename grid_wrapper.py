from numpy import ndarray
from const import GRID_SIZE, BOX_SIZE


class GridWrapper:

    def __init__(self, grid):
        self._check_grid(grid)
        self.grid = grid

    @staticmethod
    def _check_grid(grid):
        if not isinstance(grid, ndarray):
            raise TypeError("Grid expected to be an instance of numpy.ndarray, instead got: " + str(
                type(grid)))
        elif grid.shape != (GRID_SIZE, GRID_SIZE):
            raise ValueError("Grid must be of shape 9x9")
        elif 0 not in grid:
            raise ValueError("Grid is already full")

    def get_available_numbers_for_position(self, row, column):
        available_numbers = set(range(1, 10))
        used_in_row = self.get_used_in_row(row)
        used_in_column = self.get_used_in_column(column)
        used_in_box = self.get_used_in_box(row, column)
        available_numbers = available_numbers.difference(used_in_row).difference(used_in_column).difference(used_in_box)
        return available_numbers

    def get_used_in_row(self, row):
        return set(self.grid[row, :])

    def get_used_in_column(self, column):
        return set(self.grid[:, column])

    def get_used_in_box(self, row, column):
        box = self.get_box_for_cell(row, column)
        return set(box.flatten())

    def get_box_for_cell(self, row, column):
        row_start = self._get_start_index(row)
        row_end = self._get_end_index(row_start)
        column_start = self._get_start_index(column)
        column_end = self._get_end_index(column_start)
        box = self.grid[row_start:row_end, column_start:column_end]
        return box

    @staticmethod
    def _get_start_index(position):
        return position - position % BOX_SIZE

    @staticmethod
    def _get_end_index(position):
        return position + BOX_SIZE
