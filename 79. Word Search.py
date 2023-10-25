class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(board), len(board[0])
        used = set()        

        def dfs(r,c,index) -> bool:

            if index == len(word): return True
            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and board[r+dr][c+dc] == word[index] and (r+dr,c+dc) not in used:
                    used.add((r+dr,c+dc))
                    if dfs(r+dr,c+dc,index+1): return True
                    used.remove((r+dr,c+dc))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                used = set()
                if board[r][c] == word[0]: 
                    used.add((r,c))
                    if dfs(r,c,1): return True
        return False

        