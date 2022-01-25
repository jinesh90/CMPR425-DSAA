"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), retrun max area of given island
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 4

"""


def dfs(array, row, col):
    area = 1
    # set node as visited
    array[row][col] = "0"

    # iterate in all directions
    directions = [(row,col+1),(row,col-1),(row-1, col),(row+1,col)]
    for i in directions:
        # check all valid condition for recursive call
        if i[0] >= 0 and i[1] >= 0 and i[0] < len(array) and i[1] < len(array[i[0]]) and array[i[0]][i[1]] == "1":
            area += dfs(array, i[0], i[1])
    return area


def max_island_area(array):

    # area tracker of island
    island_area = [0]

    # get no of rows
    row = len(array)
    if row > 0:
        col = len(array[0])
    else:
        return 0
    # now iterate through m x n array
    for i in range(row):
        for j in range(col):
            # check if item is part of island
            if array[i][j] == "1":
                # invoke dfs
                island_area.append(dfs(array,i,j))
    return max(island_area)


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","1","0"],
  ["0","0","1","1","1"]
]
print(max_island_area(grid))




