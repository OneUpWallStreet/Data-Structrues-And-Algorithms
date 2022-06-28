class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0

        def checkDistance(v1) -> bool:
            for v2 in arr2:
                if abs(v1 - v2) <= d:
                    return False
            return True

        for v1 in arr1:
            if checkDistance(v1):
                result += 1

        return result
