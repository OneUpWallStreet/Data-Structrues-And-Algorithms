class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]
        if image[sr][sc] == color: return image

        def dfs(r,c):
            image[r][c] = color
            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and image[r+dr][c+dc] == startColor:
                    dfs(r+dr,c+dc)
        dfs(sr,sc)
        return image


# BFS 
    def BFSfloodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        rows, cols, q, ogColor, visited = len(image), len(image[0]), collections.deque(), image[sr][sc], set()

        q.append((sr,sc))

        while q:
            
            r,c = q.popleft()
            visited.add((r,c))
            image[r][c] = color

            for dr,dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and image[r+dr][c+dc] == ogColor and (r+dr,c+dc) not in visited:
                    q.append((r+dr,c+dc))

        return image
        