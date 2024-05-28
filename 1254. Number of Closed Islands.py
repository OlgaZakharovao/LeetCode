'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
'''
'''
import pprint
# 0 - island, 1 - water

def closedIsland(grid):
    def recursive(x, y):
        grid[x][y] = 1
        if x < len(grid)-1 and grid[x+1][y] == 0:
            recursive(x+1, y)
        if x > 0 and grid[x-1][y] == 0:
            recursive(x-1, y)
        if y < len(grid[0])-1 and grid[x][y+1] == 0:
            recursive(x, y+1)
        if y > 0 and grid[x][y-1] == 0:
            recursive(x, y-1)


    ans = 0
    for i in range(len(grid)):
        if grid[i][0] == 0:
            recursive(i, 0)
        if grid[i][len(grid[0])-1] == 0:
            recursive(i, len(grid[0])-1)
    for j in range(len(grid[0])):
        if grid[0][j] == 0:
            recursive(0, j)
        if grid[len(grid)-1][j] == 0:
            recursive(len(grid)-1, j)
    pprint.pprint(grid)
    print()
    print()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                recursive(i, j)
                ans += 1
    pprint.pprint(grid)
    return ans


grid = [[0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1],
        [0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1],
        [1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0],
        [0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0],
        [1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1],
        [1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1],
        [1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0],
        [1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0],
        [1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1],
        [1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0],
        [1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1],
        [0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0],
        [1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1]]

print(closedIsland(grid))
'''
# Другое решение
import pprint
# 0 - island, 1 - water

def closedIsland(grid):
   queue = [(0,0)]
   while len(queue) != 0:
        start_x, start_y = queue.pop(0)
        grid[start_x][start_y] = 1
        if start_x < len(grid) - 1 and grid[start_x + 1][start_y] == 0:
            queue.append((start_x+1, start_y))
        if start_x > 0 and grid[start_x - 1][start_y] == 0:
            queue.append((start_x - 1, start_y))
        if start_y < len(grid[0]) - 1 and grid[start_x][start_y + 1] == 0:
            queue.append((start_x, start_y+1))
        if start_y > 0 and grid[start_x][start_y - 1] == 0:
            queue.append((start_x, start_y - 1))
   return grid

grid = [[0,0,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,1,1,1,0,0,1],
        [1,1,1,0,0,1,1],
        [1,0,1,1,1,1,0]]

pprint.pprint(closedIsland(grid))