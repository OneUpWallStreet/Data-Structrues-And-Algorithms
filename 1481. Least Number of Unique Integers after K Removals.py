import collections
import heapq
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        heap = []
        hm = collections.Counter(arr)
        for key,v in hm.items(): heapq.heappush(heap,[v,key])
            
        while k > 0:
            freq, _ = heap[0]
            if freq <= k:
                heapq.heappop(heap)
                k -= freq
            else: break

        return len(heap)