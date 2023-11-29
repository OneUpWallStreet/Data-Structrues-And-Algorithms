from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and board[r+dr][c+dc] == "O" and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc)
            

        # Loop through top and bot
        for c in range(cols):
            # top
            if (0,c) not in visited and board[0][c] == "O": dfs(0,c)
            # bot
            if (rows-1,c) not in visited and board[rows-1][c] == "O": dfs(rows-1,c)
        
        # Loop through left & right 
        for r in range(rows):
            # left
            if (r,0) not in visited and board[r][0] == "O": dfs(r,0)
            
            # right
            if (r,cols-1) not in visited and board[r][cols-1] == "O": dfs(r,cols-1)
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited: board[r][c] = "X"

        
        