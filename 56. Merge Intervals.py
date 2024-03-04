class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = [intervals[0]]

        # These functions are so good. Make this problem 10 times easier 
        def isOverlap(a,b): 
            return a[0] <= b[1] and a[1] >= b[0]
        
        def merge(a,b): 
            return [min(a[0],b[0]),max(a[1],b[1])]

        for i in range(1,len(intervals)):

            top = result[-1]
            cur = intervals[i]

            if isOverlap(top,cur): 
                result.pop()
                result.append(merge(top,cur))
                
            else: result.append(intervals[i])
        
        return result