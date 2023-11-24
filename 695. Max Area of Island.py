from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                if r + dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1: 
                    s1 = len(visited)
                    dfs(r,c)
                    s2 = len(visited)
                    result = max(result,s2-s1)

        return result