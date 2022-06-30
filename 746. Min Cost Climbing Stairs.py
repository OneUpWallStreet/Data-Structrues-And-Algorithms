from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = dict()
        def dfs(index) -> int:
            if index < 0:
                return 0
            elif index in cache:
                return cache[index]
            elif index == 0 or index == 1:
                return cost[index]
            cache[index] = cost[index] + min(dfs(index-1),dfs(index-2))
            return cache[index]
        return min(dfs(len(cost)-1),dfs(len(cost)-2))
