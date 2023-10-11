class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def rcr(openC, closeC, cur):
            
            if len(cur) > n*2: return
            if (openC == n and closeC == n): 
                result.append(cur)
                return 

            rcr(openC+1,closeC, cur + "(")

            # Only if close is valid i.e. close < open
            if closeC < openC: rcr(openC,closeC+1, cur + ")")

        rcr(0,0,"")
        return result