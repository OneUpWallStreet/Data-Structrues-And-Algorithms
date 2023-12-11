class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        floorVal = len(arr) / 4

        hm = collections.defaultdict(int)

        for num in arr: 
            hm[num] += 1
            if hm[num] > floorVal: return num
        
        return -1
