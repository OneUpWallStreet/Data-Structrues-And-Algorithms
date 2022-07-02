from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                visited.remove(num)
        return visited.pop()
        
        