from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = secondLargest = float('-inf')
        for num in nums:
            if num >= largest:
                secondLargest = largest
                largest = num
            elif num > secondLargest: secondLargest = num
        return (largest-1) * (secondLargest-1)
