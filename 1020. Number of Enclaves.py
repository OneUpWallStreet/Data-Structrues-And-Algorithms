# We first remove land on edge of grid, than do another DFS 
# to count number of moves we can make.

class Solution:
    result = 0

    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r: int, c: int,isMove: bool):
            grid[r][c] = 0

            if isMove:
                self.result += 1

            for dr, dc in directions:
                if (r + dr) in range(rows) and (c + dc) in range(cols) and \
                        grid[r + dr][c + dc] == 1:
                    dfs(r + dr, c + dc, isMove)

        # Remove land on edge
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows-1 or j == cols - 1) and grid[i][j] == 1:
                    dfs(i,j,False)

        # Walk All Remaining enclaves
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j,True)

        return self.result



# Another Apporach - POST NYU ADMIT :D 

class Solution:

    isEnclave = True
    result = 0

    def numEnclaves(self, grid: List[List[int]]) -> int:

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rows, cols = len(grid),len(grid[0])
        internalSet = set()
        externalSet = set()

        def dfs(r,c):
            
            internalSet.add((r,c))
            externalSet.add((r,c))

            for (dr,dc) in directions: 
                if r+dr >= rows or r+dr < 0 or c+dc <0 or c+dc >= cols:
                    self.isEnclave = False

                if r+dr in range(rows) and \
                    c+dc in range(cols) and \
                    grid[r+dr][c+dc] == 1 and \
                    (r+dr,c+dc) not in internalSet:
                    dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                self.isEnclave = True
                if (r,c) not in externalSet and grid[r][c] == 1:
                    internalSet = set()
                    dfs(r,c)
                    if self.isEnclave == True:
                        self.result += len(internalSet)

        return self.result