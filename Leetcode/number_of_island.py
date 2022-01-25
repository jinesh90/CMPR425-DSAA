"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""


def dfs(array, row, col):
    # set node as visited
    array[row][col] = "0"

    # iterate in all directions
    directions = [(row,col+1),(row,col-1),(row-1, col),(row+1,col)]
    for i in directions:
        # check all valid condition for recursive call
        if i[0] >= 0 and i[1] >= 0 and i[0] < len(array) and i[1] < len(array[i[0]]) and array[i[0]][i[1]] == "1":
            dfs(array, i[0], i[1])


def number_of_island(array):
    # get no of rows
    row = len(array)
    if row > 0:
        col = len(array[0])
    else:
        return 0
    total_islands = 0
    # now iterate through m x n array
    for i in range(row):
        for j in range(col):
            # check if item is part of island
            if array[i][j] == "1":
                # invoke dfs
                dfs(array,i,j)
                total_islands += 1
    return total_islands


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(number_of_island(grid))




