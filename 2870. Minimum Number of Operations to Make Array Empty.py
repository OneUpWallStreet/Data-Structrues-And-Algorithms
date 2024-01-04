class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = dict()
        hm = collections.Counter(nums)
        
        def dfs(val):
            if val in cache: return cache[val]
            elif val == 2 or val == 3: return 1
            elif val <= 1: return float('inf')


            res = min(dfs(val-2),dfs(val-3))
            cache[val] = 1 + res
            return cache[val]

        result = 0
        for v in hm.values():
            res = dfs(v)

            if res == float('inf'): return -1
            result += res
        
        return result