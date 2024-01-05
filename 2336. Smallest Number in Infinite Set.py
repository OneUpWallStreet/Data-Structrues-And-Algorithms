class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [val for val in range(1,1001)]
        self.hs = set(self.heap)
        
    def popSmallest(self) -> int: 
        num = heapq.heappop(self.heap)
        self.hs.remove(num)
        return num

    def addBack(self, num: int) -> None: 
        if num not in self.hs: 
            self.hs.add(num)
            heapq.heappush(self.heap,num)
        