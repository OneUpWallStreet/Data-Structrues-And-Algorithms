class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            cur, top = intervals[i], result[-1]
            if top[1] >= cur[0]:
                result.pop()
                result.append([top[0],max(cur[1],top[1])])
            else: result.append(cur)
        return result


        
        pass
        