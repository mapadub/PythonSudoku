from grid_wrapper import GridWrapper
from const import GRID_SIZE
import copy


class Solver:

    def is_solvable(self, wrapper):
        """
        Check whether or not the grid is solvable
        :param wrapper:
        :return: True if grid is solvable
        """
        self._check_is_grid_wrapper(wrapper)
        copied_wrapper = copy.deepcopy(wrapper)
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if copied_wrapper.grid[row, column] == 0:
                    available_numbers = copied_wrapper.get_available_numbers_for_position(row, column)
                    for n in available_numbers:
                        copied_wrapper.grid[row, column] = n
                        if self.is_solvable(copied_wrapper):
                            return True  # recursive, checks if the Sudoku will be solvable after
                        copied_wrapper.grid[row, column] = 0
                    return False
        print("The grid is solvable! The solution is: \n")
        print(copied_wrapper.grid)
        return True

    @staticmethod
    def _check_is_grid_wrapper(obj):
        if not isinstance(obj, GridWrapper):
            raise TypeError("Wrapper parameter must be an instance of GridWrapper")



