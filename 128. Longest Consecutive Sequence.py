import heapq
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        heapq.heapify(nums)
        
        result = 1
        cur = heapq.heappop(nums)
        curFreq = 1
        
        while len(nums) > 0:
            if nums[0] == cur:
                cur = heapq.heappop(nums)
            elif nums[0] == cur+1:
                cur = heapq.heappop(nums)
                curFreq += 1
            else:
                curFreq = 1
                cur = heapq.heappop(nums)
            result = max(result,curFreq)

        return result
        
    def longestConsecutive2023Solution(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0

        result = 0

        hs = set()
        heapq.heapify(nums)

        for num in nums: hs.add(num)

        def findSmallest() -> int:
            cur = heapq.heappop(nums)
            # Because we don't want used values
            while cur not in hs:
                cur = heapq.heappop(nums)
            return cur
        
        sm = findSmallest()
        cur = 0

        while hs:
            
            if sm in hs:
                cur += 1
                result = max(cur,result)
                hs.remove(sm)
                sm += 1
            else:
                sm = findSmallest()
                cur = 0
                continue
            
        return result

# Solution using Heap
    def longestConsecutiveHeap2022(self, nums: List[int]) -> int:

        hashset = set()
        result = 0

        for num in nums:
            hashset.add(num)

        def getSeq(num,cur):
            if num in hashset:
                cur += 1
                return getSeq(num+1,cur)
            else:
                return cur

        for num in nums:
            if num-1 not in hashset: 
                result = max(result,getSeq(num,0))
                
        return result