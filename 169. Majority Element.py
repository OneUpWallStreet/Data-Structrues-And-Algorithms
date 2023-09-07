from typing import List
import heapq
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = dict()
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        for key,value in hashmap.items():
            if value > len(nums)/2:
                return key
            
    def heapSolutionmajorityElement(self, nums: List[int]) -> int:        
        heap, freqMap = [], collections.defaultdict(int)
        for num in nums: freqMap[num] += 1
        for k,v in freqMap.items(): heapq.heappush(heap,(-1*v,k))
        return heapq.heappop(heap)[1]
        
    def BoyerMooreAlgorithmMajorityElement(self, nums: List[int]) -> int:
        
        result = counter = 0 

        for num in nums:
            if num == result: counter += 1
            elif num != result and counter > 0: counter -= 1
            else: 
                result = num
                counter += 1

        return result