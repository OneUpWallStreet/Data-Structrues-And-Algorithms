from typing import List


# Ignore 0's on the edge
# Run DFS on all other 0's
# Need to run another DFS first to remove islands
# connected to the edge because they mess up soln


class Solution:

    result = 0

    def closedIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        alreadyVisited = set()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # We run this DFS to remove islands
        # that are on the edge because they
        # mess up the soln
        def removeIslandsOnEdge(r,c):
            alreadyVisited.add((r,c))
            grid[r][c] = 1
            for dr,dc in directions:
                if (r+dr) in range(rows) and (c+dc) in range(cols) and \
                        (r+dr,c+dc) not in alreadyVisited and grid[r+dr][c+dc] == 0:
                    removeIslandsOnEdge(r+dr,c+dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and \
                        (i == 0 or j == 0 or
                         i == rows-1 or j == cols-1) and \
                        (i,j) not in alreadyVisited:
                    removeIslandsOnEdge(i,j)

        alreadyVisited.clear()

        # DFS for finding number of islands
        def dfs(r,c):
            alreadyVisited.add((r,c))
            for dr,dc in directions:
                if (r+dr) in range(rows) and \
                        (c+dc) in range(cols) and \
                        (r+dr,c+dc) not in alreadyVisited and \
                        grid[r+dr][c+dc] == 0:
                    dfs(r+dr,c+dc)

        # Run DFS on real islands
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and \
                        (i,j) not in alreadyVisited and \
                        i != 0 and i != rows-1 and \
                        j != 0 and j != cols-1:
                    dfs(i,j)
                    self.result += 1

        return self.result
