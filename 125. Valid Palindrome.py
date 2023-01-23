class Solution:
    def isPalindrome(self, s: str) -> bool:

        paliString = ""

        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                paliString = paliString + ch.lower()
        
        first,last = 0,len(paliString)-1

        while first < last:
            if paliString[first] != paliString[last]:
                return False

            first += 1
            last -= 1
        return True