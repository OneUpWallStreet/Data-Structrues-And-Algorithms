class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        cache = dict()

        def dp(i,j):
            if (i,j) not in cache:
                if i == len(nums1) or j == len(nums2): cache[(i,j)] = 0
                elif nums1[i] == nums2[j]: cache[(i,j)] = 1 + dp(i+1,j+1)
                else: cache[(i,j)] = max(dp(i+1,j),dp(i,j+1))
            return cache[(i,j)]

        return dp(0,0)