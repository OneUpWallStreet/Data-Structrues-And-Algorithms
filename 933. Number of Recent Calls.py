class RecentCounter:

    def __init__(self):
        self.heap = []
        
    def ping(self, t: int) -> int:
        while self.heap and self.heap[0] < t - 3000: heapq.heappop(self.heap)
        heapq.heappush(self.heap,t)
        return len(self.heap) 