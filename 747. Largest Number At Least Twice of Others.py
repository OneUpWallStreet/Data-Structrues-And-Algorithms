class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for index in range(len(nums)):
            heapq.heappush(heap,[-1*nums[index],index])
        first,index1 = heapq.heappop(heap)
        second,index2 = heapq.heappop(heap)
        if (-1*first) >= (-1*second)*2:
            return index1
        else:
            return -1