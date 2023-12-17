class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        s = list(s)

        l, r = 0, len(s) - 1

        while l < len(s):
            if s[l] in vowels: break
            l += 1


        while r >= 0:
            if s[r] in vowels: break
            r -= 1

        while l <= r:

            temp = s[l] 
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1

            while l < len(s):
                if s[l] in vowels: break
                l += 1
            
            while r >= 0:
                if s[r] in vowels: break
                r -= 1
        
        return "".join(s)