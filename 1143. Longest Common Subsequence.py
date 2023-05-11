class Solution:

    # Great Explaniation by UC Irvine, I like this better than the bottom up approach
    # https://www.ics.uci.edu/~eppstein/161/960229.html

    # Memoization Solution
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        def dp(i,j):
            if cache[i][j] == -1:
                if i == len(text1) or j == len(text2): cache[i][j] = 0
                elif cache[i][j] != -1: return cache[i][j]
                elif text1[i] == text2[j]: cache[i][j] = 1 + dp(i+1,j+1)
                else: cache[i][j] = max(dp(i+1,j),dp(i,j+1))
            return cache[i][j]

        return dp(0,0)
        