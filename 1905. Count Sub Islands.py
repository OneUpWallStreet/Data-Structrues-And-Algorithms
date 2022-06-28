from typing import List

class Solution:

    result = 0
    isCurrentIslandValid = True

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(grid1)
        cols = len(grid1[0])

        def dfs(r,c):
            grid2[r][c] = 0

            if grid1[r][c] != 1:
                self.isCurrentIslandValid = False

            for dr, dc in directions:
                if (dr + r) in range(rows) and (c + dc) in range(cols) and \
                        grid2[dr + r][dc + c] == 1:
                    dfs(dr + r, dc + c)

        for i in range(0,rows):
            for j in range(0,cols):
                if grid2[i][j] == 1:
                    self.isCurrentIslandValid = True
                    dfs(i,j)
                    if self.isCurrentIslandValid:
                        self.result += 1

        return self.result
