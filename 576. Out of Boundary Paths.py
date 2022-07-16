class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
                
        directions = [[1,0],[-1,0],[0,1],[0,-1]]      
        cache = dict()

        def dfs(r,c,moveCount) -> int:
            
            if (r,c,moveCount) in cache:
                return cache[(r,c,moveCount)]

            if moveCount < 0:
                return 0 
            
            if r < 0 or c < 0 or r == m or c == n:
                return 1
                                            
            cache[(r,c,moveCount)] = dfs(r-1,c,moveCount - 1) + dfs(r+1,c,moveCount - 1) + dfs(r,c-1,moveCount - 1) + dfs(r,c+1,moveCount-1)
            return cache[(r,c,moveCount)]
        
        
        return dfs(startRow,startColumn,maxMove) % 1000000007
        
        