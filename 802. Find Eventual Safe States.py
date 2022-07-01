from typing import List
import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE,GRAY,BLACK = 0,1,2
        color = collections.defaultdict(int)
        result = []
        def dfs(node: int):
            if color[node] != WHITE:
                return color[node] == BLACK
            color[node] = GRAY
            for nextNode in graph[node]:
                if color[nextNode] == BLACK:
                    continue
                if color[nextNode] == GRAY or not dfs(nextNode):
                    return False
            color[node] = BLACK
            return True
        for node in range(len(graph)):
            if dfs(node):
                result.append(node)
        return result