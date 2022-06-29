class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        adjacencyList = dict()

        if n > len(connections)+1:
            return -1

        for i in range(n):
            adjacencyList[i] = []

        for connection in connections:
            adjacencyList[connection[0]].append(connection[1])
            adjacencyList[connection[1]].append(connection[0])

        alreadyVisited = set()

        def dfs(node: int):
            alreadyVisited.add(node)

            for nextNode in adjacencyList[node]:
                if nextNode not in alreadyVisited:
                    dfs(nextNode)

        count = 0

        for node in range(n):
            if node not in alreadyVisited:
                dfs(node)
                count += 1

        return count - 1
