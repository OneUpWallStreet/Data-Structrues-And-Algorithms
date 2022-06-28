from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 2:
                    q.append((i, j))

        time = 0

        while q:
            # Loop through the first minute
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and grid[r + dr][c + dc] == 1:
                        grid[r+dr][c+dc] = 2
                        q.append((r + dr, c + dc))

            time += 1

        # Check if fresh oranges are left
        for batch in grid:
            for orange in batch:
                if orange == 1:
                    return -1

        if time > 0:
            return time - 1
        else:
            return time
