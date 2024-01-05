class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        p1 = p2 = 0
        hm = {1: 0, 0: 0}
        result = float('-inf')
        while p2 < len(nums):
            hm[nums[p2]] += 1
            if hm[0] > 1:
                hm[nums[p1]] -= 1
                p1 += 1
            else:
                result = max(result, (p2-p1) + 1)
            p2 += 1
        return result - 1