class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        hm = collections.defaultdict(int)

        l = r = 0
        result = 0

        while r < len(s):
            
            hm[s[r]] += 1

            while hm[s[r]] > 2:
                hm[s[l]] -= 1
                l += 1
            
            result = max(result, (r-l)+1)
            r += 1
            

        return result