import numpy as np
from Solver import Solver


def main():
    grid = np.array([[0, 2, 0, 6, 0, 0, 0, 0, 5],
                     [5, 4, 9, 0, 3, 0, 8, 1, 0],
                     [0, 0, 0, 0, 8, 5, 7, 0, 0],
                     [0, 8, 0, 0, 4, 7, 9, 0, 0],
                     [0, 0, 7, 2, 1, 0, 0, 3, 0],
                     [6, 3, 0, 0, 0, 0, 0, 7, 4],
                     [0, 7, 1, 8, 6, 9, 4, 5, 3],
                     [9, 0, 0, 5, 0, 0, 0, 8, 0],
                     [0, 0, 3, 0, 2, 4, 0, 0, 0]])

    solver = Solver(grid)
    if solver.solveble():
        return
    print("The grid is not solvable :(")


if __name__ == '__main__':
    main()
