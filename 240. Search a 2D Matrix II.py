class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        row = 0
        col = len(matrix[row])-1
        
        while row<len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False