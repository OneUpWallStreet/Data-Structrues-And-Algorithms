class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        p1, p2 = 0, 1
        d = arr[p2] - arr[p1]

        while p2 < len(arr):
            if arr[p2] - arr[p1] != d:
                return False
            p1 += 1
            p2 += 1
    
        return True
