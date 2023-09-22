class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # intervals.sort(key=lambda x: x[0])
        intervals.sort()
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            top = result[-1]
            cur = intervals[i]
            if cur[0] > top[0] and cur[1] < top[1]: continue
            elif cur[0] >= top[0] and cur[1] >= top[1] and cur[0] <= top[1]:
                result.pop()
                result.append([min(top[0],cur[0]),max(cur[1],top[1])])
            else: result.append(cur)

        return result
