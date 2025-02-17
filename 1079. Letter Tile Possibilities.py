class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hs = set()
        def rcr(cur,used):
            if cur:  hs.add(cur)            
            for i in range(len(tiles)):
                if i not in used:
                    used.add(i)
                    rcr(cur+tiles[i],used)
                    used.remove(i)

        rcr("",set())
        return len(hs)
                
            