import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        heapq.heapify(nums)
        
        result = 1
        cur = heapq.heappop(nums)
        curFreq = 1
        
        while len(nums) > 0:
            if nums[0] == cur:
                cur = heapq.heappop(nums)
            elif nums[0] == cur+1:
                cur = heapq.heappop(nums)
                curFreq += 1
            else:
                curFreq = 1
                cur = heapq.heappop(nums)
            result = max(result,curFreq)

        return result
        