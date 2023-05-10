class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curSum, first,last = 0, 0,k

        for index in range(last):
            curSum += nums[index]        
            
        result = curSum

        while last < len(nums):
            curSum += nums[last] - nums[first]
            result = max(result,curSum)
            first += 1
            last += 1
            
        return result/k