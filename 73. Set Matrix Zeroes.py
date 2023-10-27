class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        rows, cols = len(matrix), len(matrix[0])

        def modifyRowCol(r,c):
            for i in range(rows):  matrix[i][c] = 0            
            for i in range(cols): matrix[r][i] = 0

        toVisit = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0: toVisit.append((r,c))
        
        for visit in toVisit: modifyRowCol(visit[0],visit[1])