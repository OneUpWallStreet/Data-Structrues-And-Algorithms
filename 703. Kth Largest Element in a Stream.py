class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, nums
        for index in range(len(nums)):
            nums[index] = -1*nums[index]
        heapq.heapify(nums)     

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-1*val)
        self.heap.sort()
        return -1*self.heap[self.k-1]