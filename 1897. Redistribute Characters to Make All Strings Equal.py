class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        hm = collections.defaultdict(int)

        for word in words:
            for ch in word: hm[ch] += 1

        for v in hm.values():
            if v % len(words) != 0: return False
        
        return True