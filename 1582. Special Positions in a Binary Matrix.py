class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        def checkRow(r,curC):
            for i in range(cols):
                if mat[r][i] == 1 and i != curC: return False
            return True

        def checkCol(c,curR):
            for i in range(rows):
                if mat[i][c] == 1 and i != curR: return False
            return True

        rows, cols = len(mat), len(mat[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1: 
                    if checkRow(r,c) and checkCol(c,r): result += 1
        
        return result