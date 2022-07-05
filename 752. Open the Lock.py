import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        graph = collections.defaultdict(list)
        
        q = collections.deque()
        invalid = set(deadends)
        
        if "0000" in invalid:
            return -1
        
    
        q.append(("0000",0))
                
        
        def fetchPositiveNumber(num) -> str:
            if num+1 > 9:
                return str(0)
            else:
                return str(num+1)

        def fetchNegativeNumber(num) -> str:
            if num -1 < 0:
                return str(9)
            else:
                return str(num-1)
        
        def nextCombinations(cur) -> List[str]:
            combinations = []
            for i in range(len(cur)):
                newWheel = cur[:i] + fetchPositiveNumber(int(cur[i])) + cur[i+1:]
                combinations.append(newWheel)
                
                newWheel = cur[:i] + fetchNegativeNumber(int(cur[i])) + cur[i+1:]
                combinations.append(newWheel)
                
            return combinations
        
        while q:
            
            cur,step = q.popleft()
            if cur == target:
                return step
            
            step += 1
            
            for nextWheel in nextCombinations(cur):
                if nextWheel not in invalid:
                    invalid.add(nextWheel)
                    q.append((nextWheel,step))
                        
        
        return -1
        