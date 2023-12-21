class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        result = float('-inf')
        points.sort()
        l, r = 0, 1

        while r < len(points):
            result = max(result,points[r][0]-points[l][0])
            l += 1 
            r += 1

        return result