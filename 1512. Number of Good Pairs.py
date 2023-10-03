class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        result = 0
    
        for p1 in range(len(nums)):
            for p2 in range(p1+1,len(nums)):
                if nums[p1] == nums[p2]: 
                    result += 1

        return result 