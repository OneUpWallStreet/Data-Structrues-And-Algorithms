class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandy = -1
        result = []

        for candy in candies:
            maxCandy = max(maxCandy,candy)

        for candy in candies:
            if candy + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)

        return result