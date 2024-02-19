class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1]]
        rows, cols = len(grid), len(grid[0])

        cache = dict()

        def dfs(r,c):

            if r == rows - 1 and c == cols - 1: return grid[r][c]
            elif (r,c) in cache: return cache[(r,c)]

            res = float('inf')

            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols):  res = min(res, dfs(r+dr,c+dc) + grid[r][c])
            
            cache[(r,c)] = res
            return res
            
        return dfs(0,0)