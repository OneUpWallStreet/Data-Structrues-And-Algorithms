class Solution:
    def minimumLength(self, s: str) -> int:
        
        l, r = 0, len(s) - 1

        while l < r:
            while l+1 < r and s[l] == s[r] and s[l+1] == s[r]: l += 1
            while r-1 > l and s[l] == s[r] and s[r-1] == s[l]: r -= 1
            if s[l] != s[r]: break
            l += 1
            r -= 1

        return (r-l) + 1