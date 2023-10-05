class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = [intervals[0]]

        for cur in intervals:
            top = result[-1]

            if (cur[0] <= top[1] and cur[1] >= top[1]) or (cur[1] < top[1]):
                result.pop()
                result.append([min(top[0],cur[0]),max(cur[1],top[1])])
            else: result.append(cur)
        
        return result

        