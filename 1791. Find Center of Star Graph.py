class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = -1
        for edge in edges:
            n = max(n,edge[0])
            n = max(n,edge[1])
            graph[edge[1]].append(edge[0])
            graph[edge[0]].append(edge[1])

        for key in graph.keys():
            if len(graph[key])==n-1:
                return key 

        