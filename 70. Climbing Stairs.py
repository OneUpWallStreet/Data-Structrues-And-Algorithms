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
    
    def climbStairsSemp2023(self, n: int) -> int:

        result, cache = 0, dict() 

        def dfs(step) -> int:
            if step == n: return 1
            elif step > n: return 0 
            elif step in cache:  return cache[step]
            cache[step] = dfs(step+1) + dfs(step+2)
            return cache[step]            

        return dfs(0)