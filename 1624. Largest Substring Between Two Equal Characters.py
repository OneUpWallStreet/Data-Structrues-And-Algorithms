import collections

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        hm = collections.defaultdict(int)
        result = float('-inf')

        for i,ch in enumerate(s):
            if ch in hm: result = max(result,len(s[hm[ch]+1:i]))
            else: hm[ch] = i
        
        return result if result != float('-inf') else -1