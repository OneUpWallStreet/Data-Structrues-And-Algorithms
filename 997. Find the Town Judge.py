import collections

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1    
        
        othersTrust = collections.defaultdict(int)
        personTrusts = collections.defaultdict(int)
        
        for node in trust:
            personTrusts[node[0]] += 1
            othersTrust[node[1]] += 1
            
        for key,value in othersTrust.items():
            if value == n-1:
                if personTrusts[key] == 0:
                    return key
        
        return -1