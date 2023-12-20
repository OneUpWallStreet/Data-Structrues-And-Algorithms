from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        l, r = 0, 1
        while r < len(prices):
            cost = money - (prices[l] + prices[r])
            if cost >= 0: return cost
            else: 
                l += 1
                r += 1
        return money
