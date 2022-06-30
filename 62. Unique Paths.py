class Solution:
    cache =dict()
    def uniquePaths(self, m: int, n: int) -> int:
        if (m,n) in self.cache:
            return self.cache[(m,n)]
        elif m == 0 or n == 0:
            return 0
        elif (m,n) == (1,1):
            return 1
        self.cache[(m,n)] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        return self.cache[(m,n)]
