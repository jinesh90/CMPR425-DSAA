"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

"""


def dfs(array,row,col,word, word_index, ha):
    # visitor mark
    #array[row][col] = "0"

    valid_direction = [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]

    for i in valid_direction:
        if i[0] >= 0 and i[1] >= 0 and i[0] < len(array) and i[1] < len(array[i[0]]) and word_index < len(word):
            if(array[i[0]][i[1]] == word[word_index]):
                ha.append(word[word_index])
                word_index += 1
                dfs(array, i[0], i[1], word, word_index,ha)
    return ha

def find_word(array, word):

    n_word = []
    ha = []
    for i in word:
        n_word.append(i)

    row  = len(array)
    col = len(array[0])
    for i in range(row):
        for j in range(col):
            if array[i][j] == n_word[0]:
                return dfs(array, i, j, n_word, 1, ha)

board =  [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "ABCB"

print(find_word(board,w))