class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = dict()
        if m == 1 and n == 1: return 1

        def dfs(r,c):
            if (r,c) in cache: return cache[(r,c)]
            elif r == (m-1) and c == (n-1): return 0
            elif r == (m-2) and c == (n-1): return 1
            elif r > m or c > n or r < 0 or c < 0: return 0
            elif r == (m-1) and c == (n-2): return 1
            elif (r,c) in cache: return cache[(r,c)]
            cache[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return cache[(r,c)]

        return dfs(0,0)