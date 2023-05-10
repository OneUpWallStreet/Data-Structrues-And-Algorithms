class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        counter,first, last = 0, 0, k
        vovels = set(('a','e','i','o','u'))

        for index in range(last):
            if s[index] in vovels:
                counter += 1

        result = counter    

        while last < len(s):
            if s[first] in vovels:
                counter -= 1
            if s[last] in vovels:
                counter += 1 
            result = max(result,counter)
            first += 1
            last += 1

        return result