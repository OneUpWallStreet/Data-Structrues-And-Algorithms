class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = defaultdict(int)
        for ch in s:
            hashmap[ch] += 1
        for ch in t:
            if ch in hashmap and hashmap[ch] > 0:
                hashmap[ch] -= 1
            elif hashmap[ch] == 0 or ch not in hashmap:
                return ch
            