class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        hashset = set()
        for car in nums:
            for val in range(car[0],car[1]+1):
                hashset.add(val)
        return len(hashset)