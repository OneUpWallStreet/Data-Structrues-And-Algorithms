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