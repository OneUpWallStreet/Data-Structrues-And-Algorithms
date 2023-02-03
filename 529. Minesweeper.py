class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        rows,cols = len(board),len(board[0])
        
        def countMines(r,c) -> int:
            mineCount = 0
            for dr,dc in directions:
                if r+dr in range(rows) and \
                    c+dc in range(cols) and \
                    board[r+dr][c+dc] == "M":
                    mineCount += 1
            return mineCount

        def revealBoard(r,c):
            if board[r][c] == "M":
                board[r][c] = "X"
                return
            elif board[r][c] == "E" and countMines(r,c) == 0:
                board[r][c] = "B"
                for dr,dc in directions:
                    if r+dr in range(rows) and \
                        c+dc in range(cols) and \
                        board[r+dr][c+dc] == "E":
                        revealBoard(r+dr,c+dc)
            elif board[r][c] == "E" and countMines(r,c) != 0:
                board[r][c] = str(countMines(r,c))

        revealBoard(click[0],click[1])
        return board
