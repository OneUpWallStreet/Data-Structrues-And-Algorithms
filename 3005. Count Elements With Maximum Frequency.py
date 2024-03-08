class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        heap = []
        hm = Counter(nums)

        for v in hm.values(): heapq.heappush(heap,-1*v)

        maxVal = heap[0]*-1
        result = 0
        
        while heap and -1*(heap[0]) == maxVal: result += -1*heapq.heappop(heap)

        return result
