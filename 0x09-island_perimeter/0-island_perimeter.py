#!/usr/bin/python3

def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                if j == 0 or grid[i][j - 1] == 0:
                    count += 1
                if j == (len(grid[0]) - 1) or grid[i][j + 1] == 0:
                    count += 1
                if i == (len(grid) - 1) or grid[i + 1][j] == 0:
                    count += 1
                if grid[i - 1][j] == 0 or i == 0:
                    count += 1

    return count
