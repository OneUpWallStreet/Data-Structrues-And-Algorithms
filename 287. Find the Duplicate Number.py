from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        def nextSlow(index: int):
            if index + 1 == len(nums):
                return 0
            else:
                return index + 1

        slow = 0
        fast = 0
        intersection = -1

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                intersection = slow
                break

        slow = 0

        while slow != intersection:
            slow = nums[slow]
            intersection = nums[intersection]

        return intersection
