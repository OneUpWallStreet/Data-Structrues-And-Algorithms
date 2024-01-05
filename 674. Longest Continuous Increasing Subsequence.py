class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        p1 = p2 = result = 0
        while p2 < len(nums):
            if p2 + 1 in range(len(nums)) and nums[p2+1] > nums[p2]: result = max(result, (p2-p1)+1)
            else: p1 = p2 + 1
            p2 += 1
        return result+1