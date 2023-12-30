class Solution:

    # Got TLE
    def myfindChampion(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)


        for edge in edges: graph[edge[0]].append(edge[1])
        visited = set()


        def dfs(node):
            visited.add(node)
            for nextNode in graph[node]: dfs(nextNode)
            return len(visited)
                

        for i in range(n):
            visited = set()
            dfs(i)
            if len(visited) == n: return i
        
        return -1


    # Solution using indegree, imp concept to know ig 
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        inDegree = [0] * n

        for edge in edges: inDegree[edge[1]] += 1


        champions = []

        for i, val in enumerate(inDegree):
            if val == 0: champions.append(i)

        return champions[0] if len(champions) == 1 else -1


