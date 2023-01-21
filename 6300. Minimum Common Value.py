class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashset = set()
        for num in nums1:
            hashset.add(num)
        for num in nums2:
            if num in hashset:
                return num
        return -1