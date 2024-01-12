class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s1,s2 = s[:int(len(s)/2)], s[int(len(s)/2):]
        v1 = v2 = 0
        vowels = set(['a','e','i','o','u'])

        for i in range(len(s1)):
            if s1[i].lower() in vowels: v1 += 1
            if s2[i].lower() in vowels: v2 += 1
        
        return v1 == v2