class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        result = [[0 for _ in range(n)] for _ in range(n)]
        
        left,right = 0,n
        top,bot = 0,n
        
        counter = 1
        
        while left < right and top < bot:
            
            for i in range(left,right):
                result[top][i] = counter
                counter += 1
            top += 1
            
            
            for i in range(top,bot):
                result[i][right-1] = counter
                counter += 1
            right -= 1
            
            if not (left < right and top < bot):
                break
                
            for i in range(right-1,left-1,-1):
                result[bot-1][i] = counter
                counter += 1
            bot -= 1
            
            for i in range(bot-1,top-1,-1):
                result[i][left] = counter
                counter += 1
            left += 1
        
            
            
        return result
        