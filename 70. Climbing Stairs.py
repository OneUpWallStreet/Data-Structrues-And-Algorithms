class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()
        def dfs(n: int):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            elif n in cache:
                return cache[n]
            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
        return dfs(n)