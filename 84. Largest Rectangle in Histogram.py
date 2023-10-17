class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = collections.deque()
        result = float('-inf')

        for index, bar in enumerate(heights):
            if not stack or stack[-1][1] < bar: stack.append((index,bar))
            else:
                firstIndex = float('inf')
                while stack and stack[-1][1] > bar:
                    oldBarIndex, oldBarHeight = stack.pop()
                    firstIndex = oldBarIndex
                    result = max(result, (index - oldBarIndex)*oldBarHeight)
                stack.append((firstIndex,bar))
        
        while stack:
            index, bar = stack.pop()
            result = max(result, (len(heights)- index)*bar)
        
        return result