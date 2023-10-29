class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        rows, cols = len(heights), len(heights[0])
        used = set()
        result = []

        def dfs(r,c,isForPacific):
            used.add((r,c))
            for dr,dc in directions:
                if isForPacific == True and (r+dr < 0 or c + dc < 0):  return True
                elif isForPacific == False and (r+dr >= rows or c + dc >= cols):  return True
                elif r+dr in range(rows) and c + dc in range(cols) and heights[r+dr][c+dc] <= heights[r][c] and (r+dr,c+dc) not in used:
                    if dfs(r+dr,c+dc,isForPacific): return True
            return False

        for r in range(rows):
            for c in range(cols):
                used = set()
                pac = dfs(r,c,True)
                used = set()
                atl = dfs(r,c,False)
                if pac and atl: result.append([r,c])        
        return result

    def pacificAtlanticBetter(self, heights: List[List[int]]) -> List[List[int]]:
        

        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,hs):

            hs.add((r,c))

            for dr, dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and heights[r+dr][c+dc] >= heights[r][c] and (r+dr,c+dc) not in hs:
                    dfs(r+dr,c+dc,hs)

        for c in range(cols):
            dfs(0,c,pac)
            dfs(rows-1,c,atl)

        for r in range(rows):
            dfs(r,0,pac)
            dfs(r,cols-1,atl)

        result = []

        for val in pac:
            if val in atl: result.append(val)

        return result