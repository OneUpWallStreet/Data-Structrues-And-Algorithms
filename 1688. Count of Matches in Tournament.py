class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        if n == 0: return 0 
        elif n == 1: return 0 
        elif n == 2: return 1

        if n % 2 == 0:
            return int((n/2) + self.numberOfMatches(n/2))
        else:
            return int((1 + ((n-1)/2)) + self.numberOfMatches(((n-1)/2)))
        
