class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        top = intervals[0]
        result = 0
        for i in range(1,len(intervals)):
            cur = intervals[i]
            if cur[0] < top[1]:
                result += 1
                if cur[1] < top[1]: top = cur
            else: top = cur
        return result