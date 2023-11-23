import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        freshOranges = 0
        q = collections.deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        timestep = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: freshOranges += 1
                elif grid[r][c] == 2: q.append((r,c))

        if freshOranges == 0: return 0 

        while q:

            for _ in range(len(q)):
                
                r,c = q.popleft()

                for dr, dc in directions:
                    if r + dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc]== 1: 
                        q.append((r+dr,c+dc))
                        grid[r+dr][c+dc] = 2
                        freshOranges -= 1
            timestep += 1

        return timestep-1 if freshOranges == 0 else -1