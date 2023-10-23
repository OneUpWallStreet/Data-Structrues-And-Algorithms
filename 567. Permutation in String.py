class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hm1 = collections.defaultdict(int)
        hm2 = collections.defaultdict(int)

        for ch in s1: hm1[ch] += 1

        l = r = 0
        while r < len(s2):
            hm2[s2[r]] += 1
            if (r-l) + 1 == len(s1):
                if hm1 == hm2: return True
                hm2[s2[l]] -= 1
                if hm2[s2[l]] == 0: del hm2[s2[l]]
                l += 1
            r += 1

        return False
