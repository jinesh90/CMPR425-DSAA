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

    # set island visited
    array[row][col] = "0"

    valid_direction = [(row,col+1),(row,col-1),(row-1, col),(row+1,col)]

    #iterarte through directions
    for i in valid_direction:
        if i[0] >= 0 and i[1] >= 0 and i[0] < len(array) and i[1] < len(array[i[0]]) and array[i[0]][i[1]] == "1":
            area += dfs(array,i[0],i[1])
    return area

def get_max_area_of_island(array):
    row = len(array)
    col = len(array[0])

    max_area = [0]

    total_area = 0
    for i in range(row):
        for j in range(col):
            if array[i][j] == "1":
                # invoke dfs
                max_area.append(dfs(array, i, j))

    max_area.append(total_area)

    return max(max_area)

grid = [ ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(get_max_area_of_island(grid))