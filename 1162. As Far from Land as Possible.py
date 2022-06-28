from typing import List
import collections


class Solution:
    result = 0

    def maxDistance(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == 0 or len(q) == rows*cols:
            return -1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and \
                            grid[r + dr][c + dc] == 0:
                        q.append((r + dr, c + dc))
                        grid[r+dr][c+dc] = 1
            self.result += 1

        return self.result-1
