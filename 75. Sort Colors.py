import collections
from typing import List

class Solution:

    def sortColorsBucket(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        bucket = [0,0,0]

        for num in nums: bucket[num] += 1
        index = 0
        for i in range(3):
            for j in range(bucket[i]):
                nums[index] = i
                index += 1
            
        

    def sortColors(self, nums: List[int]) -> None:
        
        hashmap = collections.defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
            
        counter = 0
        
        for i in range(3):
            while hashmap[i] != 0:
                nums[counter] = i
                hashmap[i] -= 1
                counter += 1    
            
            