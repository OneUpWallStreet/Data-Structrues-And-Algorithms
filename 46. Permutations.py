from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backTrackingDFS(used: set,perm: List[int]):

            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    perm.append(num)
                    backTrackingDFS(used,perm)
                    perm.pop()
                    used.remove(num)

        backTrackingDFS(set(),[])
        return result
