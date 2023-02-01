class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        visited = set()
        for num in nums1:
            visited.add(num)
        nums2.sort()
        index = 0
        while index < len(nums2):
            if index > 0 and nums2[index] == nums2[index-1]:
                index += 1
            else:
                if nums2[index] in visited:
                    result.append(nums2[index])
                index += 1
        return result