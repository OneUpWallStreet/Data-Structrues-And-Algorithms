class Solution:

    def bruteForcemaxScore(self, s: str) -> int:
        
        result = float('-inf')

        def count(val, st):
            cur = 0
            for ch in st: 
                if ch == val: cur += 1
            return cur

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                result = max(result, count("0",s[:j]) + count("1",s[j:]))
        
        return result