class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = -sys.maxsize
        p1 = p2 = 0

        while p2 < len(prices):
            
            result = max(result,prices[p2]-prices[p1])
            if prices[p1] > prices[p2]: p1 += 1
            else: p2 += 1

        return result
