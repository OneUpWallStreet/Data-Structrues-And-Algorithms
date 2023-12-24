class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set(["a","e","i","o","u"])
        ctr = 0
        for i in range(k):
            ch = s[i]
            if ch in vowels: ctr += 1
        
        result = ctr

        l, r = 0, k

        while r < len(s):

            
            if s[r] in vowels: ctr += 1
            if s[l] in vowels: ctr -= 1

            result = max(result,ctr)

            r += 1
            l += 1


        return result
        

