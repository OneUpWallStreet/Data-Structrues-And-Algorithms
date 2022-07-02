from typing import List

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
            
        