class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        for i in range(1,n+1):
            if n % i == 0: heapq.heappush(heap,i)
        return heap[k-1] if k-1 < len(heap) else -1