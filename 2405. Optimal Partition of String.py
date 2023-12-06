class Solution:
    def partitionString(self, s: str) -> int:
        hs = set()
        result = 1
        for i in range(len(s)):
            if s[i] in hs:
                result += 1
                hs = set()
            hs.add(s[i])
        return result