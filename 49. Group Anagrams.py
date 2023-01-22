class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashset = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            hashset[sortedStr].append(s)
        for value in hashset.values():
            result.append(value)
        return result