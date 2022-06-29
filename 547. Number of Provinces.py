from typing import List

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = dict()

        for index in range(len(isConnected)):
            if index + 1 not in graph:
                graph[index + 1] = []
            for nodeIndex in range(len(isConnected[index])):
                if isConnected[index][nodeIndex] == 1:
                    graph[index + 1].append(nodeIndex + 1)

        count = 0
        visitedSet = set()

        def dfs(node: int):
            visitedSet.add(node)
            for nextNode in graph[node]:
                if nextNode not in visitedSet:
                    dfs(nextNode)

        for key, value in graph.items():
            if key not in visitedSet:
                dfs(key)
                count += 1

        return count
