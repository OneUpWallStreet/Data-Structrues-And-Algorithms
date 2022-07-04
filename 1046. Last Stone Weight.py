import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]

        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if x == y:
                continue
            else:
                heapq.heappush(stones,y-x)


        if len(stones) == 1:
            return -1*heapq.heappop(stones)
        else:
            return 0
        
        