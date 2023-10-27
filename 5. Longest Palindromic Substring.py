class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""

        def findPalindrome(l,r):
            cur = ""

            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                cur = s[l:r+1]
                l -= 1
                r += 1
            return cur
        
        for i in range(len(s)):
            odd = findPalindrome(i,i)
            even = findPalindrome(i,i+1) 
            result = max(odd,even,key=len) if len(max(odd,even,key=len)) > len(result) else result

        return result
        