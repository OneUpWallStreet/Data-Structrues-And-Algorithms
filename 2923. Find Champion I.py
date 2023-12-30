from typing import List
import collections

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: graph[j].append(i)
                
        for i in range(n):
            if i not in graph: return i