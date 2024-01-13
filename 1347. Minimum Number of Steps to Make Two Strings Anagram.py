class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sMap, tMap = collections.Counter(s), collections.Counter(t)
        result = 0
        for ch in set(sMap.keys()).union(set(tMap.keys())): result += max(tMap[ch] - sMap[ch],0)
        return result