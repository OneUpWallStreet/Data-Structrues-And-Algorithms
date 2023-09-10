class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, result = 0, float(-inf)
        for num in nums:
            if curSum < 0: curSum = 0
            curSum += num
            result = max(curSum,result)
        return result