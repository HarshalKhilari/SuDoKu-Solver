import numpy as np


def solve_sudoku(grid):
    grid = np.array(grid, dtype='int')
    print(solve(grid))


def solve(grid):
    # Main function to solve sudoku
    while is_any_unfilled(grid):
        for row_num in range(9):
            for col_num in range(9):
                if grid[row_num, col_num] == 0:
                    grid[row_num, col_num] = check_values(grid, row_num, col_num)
    return grid


def is_any_unfilled(grid):
    # Function to check if any cell is left unfilled
    for row_num in range(9):
        for col_num in range(9):
            if grid[row_num, col_num] == 0:
                return True
    return False


def check_values(grid, row_num, col_num):
    # Function to check for and return a single number as solution for the cell
    seen = []
    for i in grid[row_num]:
        seen.append(i)
    for i in range(9):
        seen.append(grid[i, col_num])
    subgrid_first_row = row_num - row_num % 3
    subgrid_first_col = col_num - col_num % 3
    subgrid = grid[subgrid_first_row:subgrid_first_row + 3, subgrid_first_col:subgrid_first_col + 3]
    for i in subgrid.flatten():
        seen.append(i)
    possibles = []
    for i in range(1, 10):
        if i not in seen:
            possibles.append(i)
    if len(possibles) == 1:
        return possibles[0]
    return 0
