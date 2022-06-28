from typing import List

class Solution:
    maxArea = 0
    currentIslandArea = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        alreadyVisited = set()

        def dfs(r, c):

            self.currentIslandArea += 1

            self.maxArea = max(self.maxArea, self.currentIslandArea)
            alreadyVisited.add((r, c))
            for dr, dc in directions:
                if (r + dr) in range(rows) and \
                        (c + dc) in range(cols) and \
                        (r + dr, c + dc) not in alreadyVisited and \
                        grid[r + dr][c + dc] == 1:
                    dfs(r + dr, c + dc)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1 and (i, j) not in alreadyVisited:
                    self.currentIslandArea = 0
                    dfs(i, j)

        return self.maxArea

