'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no
vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to
destination, or false otherwise.



Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
'''

'''
from collections import defaultdict


def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    l = defaultdict(list)

    for i, j in edges:
        l[i].append(j)
        l[j].append(i)

    s = set()

    def dfs(node):
        if node == destination:
            return True
        s.add(node)
        for j in l[node]:
            if j not in s and dfs(j):
                return True
        return False

    return dfs(source)
'''
from collections import defaultdict


def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # DFS
    stack = [source]
    visited = [source]
    edges_dict = defaultdict(list)
    for edge in edges:
        edges_dict[edge[0]].append(edge[1])
        edges_dict[edge[1]].append(edge[0])

    while len(stack) > 0:
        if stack[0] == destination:
            return True
        for i in (edges_dict[stack[0]]):
            if i not in stack and i not in visited:
                stack.append(i)
                visited.append(i)
        stack.pop(0)
    return False


# n = 3
# edges = [[0, 1], [1, 2], [2, 0]]
# source = 0
# destination = 2
# print(validPath(n, edges, source, destination))
print(validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))

'''
    Попытка 1

    '''
