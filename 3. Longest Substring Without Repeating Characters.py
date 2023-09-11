class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0

        result = l = r = 0 

        seen = set()

        while r < len(s):
            
            if s[r] in seen: 
                seen.remove(s[l])
                l += 1
                continue

            result = max(result,r-l)
            seen.add(s[r])
            r+= 1             

            

        return result+1