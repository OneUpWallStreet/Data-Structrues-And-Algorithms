class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = result = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: 
                cur += nums[i]
                result = max(result,cur)
            else: 
                cur = nums[i]
        return result