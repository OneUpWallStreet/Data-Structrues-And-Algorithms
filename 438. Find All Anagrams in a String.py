from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pDict = collections.Counter(p)
        sDict = collections.Counter(s[:len(p)])
        result = []
        start = 0
        end = len(p)

        while end <= len(s):
            if pDict == sDict:
                result.append(start)
            sDict[s[start]] -= 1
            if sDict[s[start]] <= 0:
                sDict.pop(s[start])
            if end < len(s):
                sDict[s[end]] += 1
            start += 1
            end += 1
        return result