class Solution:
    def isPathCrossing(self, path: str) -> bool:

        dim = (0,0)
        hs = set()
        hs.add((0,0))

        directions = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0)
        }

        for cur in path:
            dr, dc = directions[cur]
            if (dim[0] + dr, dim[1] + dc) in hs: return True
            hs.add((dim[0] + dr, dim[1] + dc))
            dim = (dim[0] + dr, dim[1] + dc)
        
        return False
