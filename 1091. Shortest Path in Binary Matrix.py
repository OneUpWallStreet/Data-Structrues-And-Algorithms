class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        q = collections.deque()
        visited = set()

        directions = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        rows,cols = len(grid), len(grid[0])

        q.append((0,0,1))

        while q:
            r, c, pathLen = q.popleft()

            if r == rows-1 and c == cols-1:
                return pathLen

            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and (r+dr,c+dc) not in visited and grid[r+dr][c+dc] == 0:
                    q.append((r+dr,c+dc,pathLen+1))
                    visited.add((r+dr,c+dc))

        return -1