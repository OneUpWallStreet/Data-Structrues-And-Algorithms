import collections

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
                
        cache = collections.defaultdict(bool)
        
        def dfs(i,j) ->bool:
            
            if i+j >= len(s3) and i == len(s1) and j == len(s2):
                return True
            elif (i,j) in cache:
                return cache[(i,j)]
            elif i + j >= len(s3):
                return False
            
            if i < len(s1) and s1[i] == s3[i+j]:
                cache[(i+1,j)] = dfs(i+1,j)
                
            if j < len(s2) and s2[j] == s3[i+j]:
                cache[(i,j+1)] = dfs(i,j+1)
                
            return cache[(i+1,j)] or cache[(i,j+1)]

        return dfs(0,0)
                