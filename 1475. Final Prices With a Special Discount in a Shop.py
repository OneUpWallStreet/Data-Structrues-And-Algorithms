class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        result = [0]*len(prices)

        def findDiscount(index) -> int:
            if index+1 == len(prices): return 0
            currentValue = prices[index]
            index += 1
            while index < len(prices):
                if prices[index] <= currentValue: return prices[index]
                index += 1
            return 0

        for index in range(len(prices)):
            result[index] = prices[index] - findDiscount(index)

        return result