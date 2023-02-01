class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        visited = set()
        for num in nums:
            if num not in visited:
                heapq.heappush(heap,-1*num)
                visited.add(num)
        if len(heap) < 3:
            return -1*heapq.heappop(heap)
        for i in range(2):
            heapq.heappop(heap)
        return -1*heapq.heappop(heap)