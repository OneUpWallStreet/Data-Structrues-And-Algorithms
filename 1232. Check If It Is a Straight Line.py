class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        slope, x1, y1 = None, coordinates[0][0], coordinates[0][1]

        def calcSlope(x2,y2):
            if (x2-x1) == 0: return None
            return (y2-y1)/(x2-x1)

        for index in range(1,len(coordinates)):
            x2, y2 = coordinates[index][0], coordinates[index][1]
            if index == 1: 
                slope = calcSlope(x2,y2)
                continue        
            elif slope != calcSlope(x2,y2): return False

        return True