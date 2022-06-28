from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrackingDFS(index: int,curArray: List[int]):
            if index >= len(nums):
                result.append(curArray[:])
                return
            # Add Element To Array
            curArray.append(nums[index])
            backtrackingDFS(index+1,curArray)
            # Backtrack
            curArray.pop()
            backtrackingDFS(index+1,curArray)
        backtrackingDFS(0,[])
        return result