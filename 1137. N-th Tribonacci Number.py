class Solution:
    def tribonacci(self, n: int) -> int:
        cache = dict()
        def dp(num):
            if num < 0 or num == 0:
                return 0
            elif num == 1 or num == 2:
                return 1
            elif num in cache:
                return cache[num]
            cache[num] = dp(num-1) + dp(num-2) + dp(num-3)
            return cache[num]
        return dp(n)