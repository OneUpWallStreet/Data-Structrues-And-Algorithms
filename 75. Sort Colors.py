import collections

class Solution:
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
            
            