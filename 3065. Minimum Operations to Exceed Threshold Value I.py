class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        result = 0
        
        while nums and nums[0] < k: 
            result += 1
            heapq.heappop(nums)
        return result
