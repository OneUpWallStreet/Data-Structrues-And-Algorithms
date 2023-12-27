from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        s1, s2 = set(nums1), set(nums2)

        result = [[],[]]

        for i in range(len(nums1)):
            if nums1[i] not in s2: 
                s2.add(nums1[i])
                result[0].append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in s1:
                s1.add(nums2[i])
                result[1].append(nums2[i])
            
        return result
