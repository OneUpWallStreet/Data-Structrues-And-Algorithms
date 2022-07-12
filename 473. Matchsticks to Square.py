class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
                
        sideLen = sum(matchsticks) // 4
        
        if sum(matchsticks) / 4 != sideLen:
            return False
        
        matchsticks.sort(reverse=True)
        
#       0 - Left 
#       1 - Right
#       2 - Top
#       3 - Bottom
        dimensions = [0,0,0,0]
        
        def backtracking(index) -> bool:
            
            if index == len(matchsticks):
                return True
            
            for side in range(len(dimensions)):
                if matchsticks[index] + dimensions[side] <= sideLen:
                    dimensions[side] += matchsticks[index]
                    if backtracking(index+1):
                        return True
                    dimensions[side] -= matchsticks[index]
                    
            return False
        return backtracking(0)
        