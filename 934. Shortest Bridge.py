from typing import List
import collections

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        firstIslandSet = set()

        def dfs(r, c):
            firstIslandSet.add((r, c))
            for dr, dc in directions:
                if (r + dr) in range(rows) and (c + dc) in range(cols) and \
                        (r + dr, c + dc) not in firstIslandSet and grid[r + dr][c + dc] == 1:
                    dfs(r + dr, c + dc)

        def bfs() -> int:
            q = collections.deque()
            secondIslandSet = set()
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in firstIslandSet:
                        q.append((i, j))
            path = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if (r, c) in firstIslandSet:
                        return path
                    for dr, dc in directions:
                        if (r + dr) in range(rows) and (c + dc) in range(cols) and \
                                (r + dr, c + dc) not in secondIslandSet and \
                                (grid[r + dr][c + dc] == 0 or (r+dr,c+dc) in firstIslandSet):
                            q.append((r + dr, c + dc))
                            secondIslandSet.add((r + dr, c + dc))
                path += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in firstIslandSet:
                    dfs(i, j)
                    print(firstIslandSet)
                    return bfs()-1
