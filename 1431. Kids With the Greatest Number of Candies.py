class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        for i,candy in enumerate(candies):
            if candy + extraCandies >= maxCandy: candies[i] = True
            else: candies[i] = False
        return candies