class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for r in range(len(grid)):
            for c in range(len(grid[r])): grid[r][c] = -1*grid[r][c]


        for i in range(len(grid)): heapq.heapify(grid[i])

        result = 0
        while len(grid[0]) > 0:
            
            curMax = 0
            for i in range(len(grid)):
                curMax = max(curMax, -1*heapq.heappop(grid[i]))
                
            result += curMax

        return result