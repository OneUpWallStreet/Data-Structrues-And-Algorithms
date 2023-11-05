class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right-left):
                top, bot = left, right
                topLeft = matrix[top][left+i] 
                matrix[top][left+i] = matrix[bot-i][left]
                matrix[bot-i][left] = matrix[bot][right-i]
                matrix[bot][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft
            left += 1
            right -= 1

