from const import GRID_SIZE, BOX_SIZE


class Solver:

    def __init__(self, grid):
        self.grid = grid

    def solveble(self):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if self.grid[row][column] == 0:
                    available_numbers = self._get_available_numbers_for_position(row, column)
                    for n in available_numbers:
                        self.grid[row][column] = n
                        if self.solveble():
                            return True  # recursive, checks if the Sudoku will be solvable after
                        self.grid[row][column] = 0
                    return False
        print("The grid is solvable! The solution is: \n")
        print(self.grid)
        return True

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

    def solve_grid(self, grid):
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if not value in (
                        grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                        grid[6][col], grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                myPen.clear()
                                drawGrid(grid)
                                myPen.getscreen().update()
                                if checkGrid(grid):
                                    print("Grid Complete and Checked")
                                    return True
                                else:
                                    if solveGrid(grid):
                                        return True
                break
        print("Backtrack")
        grid[row][col] = 0
