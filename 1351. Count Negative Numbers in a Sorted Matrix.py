class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            counter, left, right = 0, 0, len(row)-1
            while left <= right:
                mid = left + (right-left)//2
                if row[mid] >= 0:  left = mid+1
                else:
                    counter = max(counter,len(row)-mid)
                    right = mid - 1
            result += counter
        return result
        
