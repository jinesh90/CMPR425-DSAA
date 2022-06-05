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


def dfs(array,row,col):
    # mark visited
    array[row][col] = "0"

    directions = [(row,col+1),(row,col-1),(row-1, col),(row+1,col)]
    for i in directions:
        if i[0] >= 0 and i[1] >= 0 and i[0] < len(array) and i[1] < len(array[i[0]]) and array[i[0]][i[1]] == "1":
            dfs(array, i[0], i[1])



def find_number_of_island(arr):
    row = len(arr)
    col = len(arr[0])
    total_number_of_island = 0
    for i in range(row):
        for j in range(col):
            # if encountered 1 invoke dfs
            if arr[i][j] == "1":
                # invoked dfs
                dfs(arr, i, j)
                total_number_of_island += 1

    return total_number_of_island

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(find_number_of_island(grid))