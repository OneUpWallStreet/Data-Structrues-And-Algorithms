import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = collections.defaultdict(int)
        
        left = 0
        result = 0
        
        def findMaxFreq() -> int:
            maxFreq = -1
            for key,value in hashmap.items():
                maxFreq = max(maxFreq,value)
            return maxFreq
        
        for right in range(len(s)):
                        
            hashmap[s[right]]+=1
            
            if (right-left+1) - findMaxFreq() > k:
                hashmap[s[left]] -= 1
                left += 1
                
            result = max(result,right-left+1)
            
        return result
        