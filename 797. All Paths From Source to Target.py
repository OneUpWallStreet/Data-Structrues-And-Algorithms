import copy
from typing import List
import collections

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        rows = len(graph)
        cols = len(graph[0])
        result = []
        q = collections.deque()
        q.append((0,[]))
        while q:
            cur,path = q.popleft()
            path.append(cur)
            if cur == len(graph)-1:
                result.append(path[:])
            for node in graph[cur]:
                q.append((node,copy.deepcopy(path)))
        return result
