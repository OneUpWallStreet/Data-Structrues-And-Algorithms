class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        result = 0
        vowels = set('aeiou')

        
        for start in range(len(s)):
            vCount = cCount = 0

            for end in range(start,len(s)):
                
                if s[end] in vowels: vCount += 1
                else: cCount += 1


                if vCount == cCount and (cCount * vCount) % k == 0: result += 1
        
        return result