class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        cache = dict()
        goalR, goalC = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        if obstacleGrid[0][0] == 1 or obstacleGrid[goalR][goalC] == 1: return 0

        def rcr(r,c):
            if r == goalR and c == goalC: return 1
            elif r > goalR or c > goalC: return 0
            elif obstacleGrid[r][c] == 1: return 0
            elif (r,c) in cache: return cache[(r,c)]
            cache[(r,c)] = rcr(r+1,c) + rcr(r,c+1)
            return cache[(r,c)]
        
        return rcr(0,0)