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

# 2023 Solution 
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        hashmap = defaultdict(list)
        personSet = set()

        if n == 1:
            return 1

        for person,trustPerson in trust:
            personSet.add(person)
            hashmap[trustPerson].append(person)
        
        for key,value in hashmap.items():
            if len(value) == n-1 and key not in personSet:
                return key

        return -1