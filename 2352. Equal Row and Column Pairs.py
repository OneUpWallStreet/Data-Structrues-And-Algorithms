class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rowHashMap = defaultdict(int)
        result = 0

        for row in grid:
            rowStr = ""
            for val in row:
                rowStr += "#" + str(val)
            rowHashMap[rowStr] += 1

        for rowIndex in range(len(grid[0])):
            colStr = ""
            for colIndex in range(len(grid)):
                colStr += "#" + str(grid[colIndex][rowIndex])
            if colStr in rowHashMap:
                result += rowHashMap[colStr]
        
        return result
    
    # My own hashing solution, this just means that I did not look at other solns lol
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        result = 0
        rows, cols = len(grid), len(grid[0])
        rHM, cHM = dict(), dict()

        def insertRow(r):
            s = ""
            for i in range(len(grid[r])): s += str(grid[r][i]) + "#"
            rHM[r] = s
        
        def insertCol(c):
            s = ""
            for i in range(rows): s += str(grid[i][c]) + "#"
            cHM[c] = s

        for r in range(rows):
            for c in range(cols):
                if r not in rHM: insertRow(r)
                if c not in cHM: insertCol(c)
                if rHM[r] == cHM[c]: result += 1


        return result

    # Came up with it but no hashing 
    def bruteForceSolnequalPairs(self, grid: List[List[int]]) -> int:
        
        result = 0


        rows, cols = len(grid), len(grid[0])

        def check(r,c):
            rArr = []
            cArr = []

            for i in range(rows):
                cArr.append(grid[i][c])
            for i in range(len(grid[r])):
                rArr.append(grid[r][i])

            return rArr == cArr


        for r in range(rows):
            for c in range(cols):
                if check(r,c): result += 1



        return result