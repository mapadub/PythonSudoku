import numpy as np
from random import randint
from const import GRID_SIZE, LEVELS
from grid_wrapper import GridWrapper
from solver import Solver



class Generator:

    def __init__(self, level):
        self._check_level_is_valid(level)
        self.level = level

    @staticmethod
    def _check_level_is_valid(obj):
        if not isinstance(obj, int):
            raise TypeError("level must be an int, instead got: " + str(type(obj)))
        elif obj not in LEVELS.values():
            raise TypeError("level must be adhere to predefined levels. Possible levels:\n "
                            + str(LEVELS))

    def generate_grid(self):
        #TODO
        pass

    def _fill_grid(self, grid):
        #TODO
        pass

    def _remove_cells(self, wrapper):
        #TODO testing
        solver = Solver()
        for i in range(self.level):
            # select random cell from grid
            row = randint(0, GRID_SIZE)
            column = randint(0, GRID_SIZE)
            cell_value = wrapper.grid[row, column]
            if cell_value != 0:
                wrapper.grid[row, column] = 0
                if not solver.is_solvable(wrapper):
                    wrapper.grid[row, column] = cell_value
