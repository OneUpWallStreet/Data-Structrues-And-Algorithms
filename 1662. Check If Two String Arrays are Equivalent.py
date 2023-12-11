from typing import List

class Solution:

    # Naive solution - O(n) time, O(n) space
    def arrayStringsAreEqualNaive(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
    
    # Two pointers - O(n) time, O(1) space
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        wp1 = wp2 = cp1 = cp2 = 0

        while wp1 < len(word1) and wp2 < len(word2):
            
            w1, w2 = word1[wp1], word2[wp2]

            while cp1 < len(w1) and cp2 < len(w2):
                if w1[cp1] != w2[cp2]: return False
                cp1 += 1
                cp2 += 1

            if cp1 >= len(w1): 
                cp1 = 0
                wp1 += 1
            
            if cp2 >= len(w2):
                cp2 = 0 
                wp2 += 1

        return wp1 == len(word1) and wp2 == len(word2)
