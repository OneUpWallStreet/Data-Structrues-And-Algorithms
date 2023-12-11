class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        for r in range(cols): result.append([0]*rows)
        for r in range(rows):
            for c in range(cols): result[c][r] = matrix[r][c]
        return result
        