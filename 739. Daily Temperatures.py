class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        hm = dict()
        stack = collections.deque()
        result = [0]*len(temperatures)

        for temp in temperatures: stack.append(temp)

        def checkForHotterDays(curTemp: int):
            minIndex = float('inf')
            for temp in range(curTemp+1,101):
                # This returns index of higher temp
                if temp in hm: 
                    minIndex = min(minIndex,hm[temp])
            if minIndex == float('inf'): return 0 
            else: return minIndex

        index = len(temperatures)-1

        while stack:
            curTemp = stack.pop()
            hotter = checkForHotterDays(curTemp)
            if hotter == 0: result[index] = 0
            else: result[index] = hotter - index
            
            hm[curTemp] = index
            index -= 1
            
        return result