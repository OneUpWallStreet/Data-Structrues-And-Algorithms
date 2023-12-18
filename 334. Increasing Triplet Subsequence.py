class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        # The third value will try to be num
        for num in nums:
            if num <= first: first = num
            elif num <= second: second = num
            # we found a num that's first < second < num
            else: return True
        return False