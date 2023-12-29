class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        if len(jobDifficulty) < d: return -1
        cache = dict()

        def rcr(i,d,curMax):
            
            # Every job is considered 
            if i == len(jobDifficulty): return 0 if d == 0 else float('inf')
            # Did not complete all jobs
            elif d == 0: return float('inf')
            elif (i,d,curMax) in cache: return cache[(i,d,curMax)]

            curMax = max(curMax,jobDifficulty[i])

            res = min(
                # Split
                curMax + rcr(i+1,d-1,float('-inf')),
                # Continue Same Day
                rcr(i+1,d,curMax)
            )

            cache[(i,d,curMax)] = res

            return res

        return rcr(0,d,float('-inf'))

