class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zCount = oCount = 0

        l = r = 0
        result = 0

        while r < len(nums):
            
            if nums[r] == 0: zCount += 1
            else: oCount += 1
            
            if zCount <= k: result = max(result, (r-l)+1)
            else:
                if nums[l] == 0: zCount -= 1
                else: oCount -= 1
                l += 1
            
            r += 1

        return result

