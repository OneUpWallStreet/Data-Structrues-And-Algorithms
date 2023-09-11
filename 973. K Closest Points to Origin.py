import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result, heap = [], []

        for index in range(len(points)):
            dist = (points[index][0]*points[index][0]) + (points[index][1]*points[index][1])
            heapq.heappush(heap,[dist,index])
        
        while k > 0:
            result.append(points[heapq.heappop(heap)[1]])
            k -= 1

        return result
