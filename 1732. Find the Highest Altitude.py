class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0 
        result = 0
        for i in range(len(gain)):
            cur += gain[i]
            result = max(result,cur)
        return result