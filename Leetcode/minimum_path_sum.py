"""
leetcode: 64
 grid = [[1,3,1],[1,5,1],[4,2,1]]
 op 7
 grid = [[1,2,3],[4,5,6]]
 op
 12
"""


def minimum_path_sum(grid):
    # create the array that has same dim
    n = len(grid)
    if n > 1:
        m = len(grid[0])

    # create result array
    result = [[0]* m for x in range(n)]

    # now start compute with assign result array to start co-ordinate.

    result[0][0] = grid[0][0]

    for i in range(1, n):
        result[i][0] = result[i-1][0] + grid[i][0]

    for j in range(1, m):
        result[0][j] = result[0][j-1] + grid[0][j]

    for i in range(1, n):
        for j in range(1, m):
            result[i][j] = grid[i][j] + min(result[i-1][j], result[i][j-1])

    return result[-1][-1]


grid =[[1,2,3],[4,5,6]]
assert minimum_path_sum(grid) == 12
grid = [[1,3,1],[1,5,1],[4,2,1]]
assert minimum_path_sum(grid) == 7