class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 1
        result = 0 
        while r < len(colors):
            if colors[l] == colors[r]: 
                result += min(neededTime[l],neededTime[r])
                neededTime[r] = max(neededTime[l],neededTime[r])
            l += 1
            r += 1
        return result