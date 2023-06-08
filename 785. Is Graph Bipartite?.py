class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # -1 for blue
        #  1 for green
        colors = [0]*len(graph)
        result = True

        def flip(color: int) -> int:
            if color == 1: return -1
            else: return 1

        def dfs(node,color) -> bool:
            nonlocal result
            colors[node] = color
            for nextNode in graph[node]:
                if colors[nextNode] == 0: dfs(nextNode,flip(color))
                elif colors[nextNode] == color: result = False

        # Ideally, we can start from the 0th node and it will work. However, sometimes the graph
        # is disconnected, so we may encounter issues. I wish the description were clearer.
        for node in range(len(graph)):
            colors = [0]*len(graph)
            dfs(node,1)
            
        return result
