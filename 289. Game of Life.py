'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead
(represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


Example 1:
Input: board = [[0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]]
Output: [[0,0,0],
         [1,0,1],
         [0,1,1],
         [0,1,0]]

Example 2:
Input: board = [[1,1],
                [1,0]]
Output: [[1,1],
         [1,1]]
'''

from pprint import pprint

def gameOfLife(board):
    neighbours = 0
    len_column = len(board[0])
    neighbours_num = [[0] * len_column for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len_column):
            cur_cell = board[i][j]
            if i < len(board) - 1 and board[i+1][j] == 1:
                neighbours += 1
            if j < len_column - 1 and board[i][j+1] == 1:
                neighbours += 1
            if i > 0 and board[i-1][j] == 1:
                neighbours += 1
            if j > 0 and board[i][j-1] == 1:
                neighbours += 1
            if i < len(board) - 1 and j < len_column - 1 and board[i+1][j+1] == 1:
                neighbours += 1
            if i > 0 and j > 0 and board[i-1][j-1] == 1:
                neighbours += 1
            if i < len(board) - 1 and j > 0 and board[i+1][j-1] == 1:
                neighbours += 1
            if i > 0 and j < len_column - 1 and board[i-1][j+1] == 1:
                neighbours += 1
            neighbours_num[i][j] = neighbours
            neighbours = 0
    for i in range(len(board)):
        for j in range(len_column):
            if neighbours_num[i][j] < 2 or neighbours_num[i][j] > 3:
                board[i][j] = 0
            elif neighbours_num[i][j] == 3 and board[i][j] == 0:
                board[i][j] = 1
    pprint(neighbours_num)
    #print(*board, sep = '\n')

board = [[1,1], [1,0]]
gameOfLife(board)
print(*board, sep = '\n')



