from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node: int,path: List[int]):
            if node == len(graph)-1:
                result.append(path[:])
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(nextNode,path)
                path.pop()
        dfs(0,[0])
        return result