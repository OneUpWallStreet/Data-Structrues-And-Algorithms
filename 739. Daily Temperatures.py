from typing import List
import collections

class Solution:
    
    def dailyTemperaturesStack(self, temperatures: List[int]) -> List[int]:

        result = [-1] * len(temperatures)
        stack = collections.deque()

        for i,temp in enumerate(temperatures):
            if stack and stack[-1][0] > temp:  stack.append((temp,i))
            else:
                while stack and stack[-1][0] < temp:
                    _, oldIndex = stack.pop()
                    result[oldIndex] = i - oldIndex
                stack.append((temp,i))
        while stack: result[stack.pop()[1]] = 0
        return result

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