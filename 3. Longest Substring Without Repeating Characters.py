class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0
        
        seen = set()

        l = r = result = 0

        while r < len(s):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            result = max(result,r-l)
            seen.add(s[r])
            r += 1

        return result + 1 
            