from numpy import ndarray
from const import GRID_SIZE, BOX_SIZE


class Solver:

    grid = None
    checked = False

    def is_solvable(self, grid):
        self._check_grid(grid)
        self.grid = grid
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if self.grid[row][column] == 0:
                    available_numbers = self._get_available_numbers_for_position(row, column)
                    for n in available_numbers:
                        self.grid[row][column] = n
                        if self.is_solvable(self.grid):
                            return True  # recursive, checks if the Sudoku will be solvable after
                        self.grid[row][column] = 0
                    return False
        print("The grid is solvable! The solution is: \n")
        print(self.grid)
        return True

    def _check_grid(self, grid):
        if not self.checked:
            if not isinstance(grid, ndarray) or grid.shape != (9, 9):
                raise TypeError("Grid parameter must be an instance of numpy.ndarray and have a 9x9 shape")
            elif 0 not in grid:
                raise ValueError("Grid is already full")
            self.checked = True

    def _get_available_numbers_for_position(self, row, column):
        available_numbers = set(range(1, 10))
        used_in_row = self._get_used_in_row(row)
        used_in_column = self._get_used_in_column(column)
        used_in_box = self._get_used_in_box(row, column)
        available_numbers = available_numbers.difference(used_in_row).difference(used_in_column).difference(used_in_box)
        return available_numbers

    def _get_used_in_row(self, row):
        return set(self.grid[row, :])

    def _get_used_in_column(self, column):
        return set(self.grid[:, column])

    def _get_used_in_box(self, row, column):
        box = self._get_box(row, column)
        return set(box.flatten())

    def _get_box(self, row, column):
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
