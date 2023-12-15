from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hs = set()
        for path in paths: hs.add(path[0])
        for path in paths: 
            if path[1] not in hs: return path[1]