'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of
the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by
a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
'''


def floodFill(image: list[list[int]], sr, sc, color) -> list[list[int]]:
    colour = image[sr][sc]
    if colour == color:
        return image
    queue = [(sr, sc)]
    while queue:
        x, y = queue.pop(0)
        image[x][y] = color
        if x < len(image) - 1 and image[x+1][y] == colour:
            queue.append((x+1, y))
        if x > 0 and image[x-1][y] == colour:
            queue.append((x - 1, y))
        if y > 0 and image[x][y-1] == colour:
            queue.append((x, y-1))
        if y < len(image[0]) - 1 and image[x][y+1] == colour:
            queue.append((x, y+1))
        print(queue)
        print(*image, sep = '\n')
        print()
    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(image,sr, sc, color))
