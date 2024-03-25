class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val-1] < 0: 
                result.append(val)
                continue
            nums[val-1] = -nums[val-1]
        
        return result 