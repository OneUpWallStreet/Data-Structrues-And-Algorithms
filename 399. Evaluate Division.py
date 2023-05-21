class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        result = []

        # Task 1 -> Create Graph
        graph = defaultdict(list)
        visited = set()

        for index in range(len(equations)):
            graph[equations[index][0]].append({
                "variable": equations[index][1],
                "value": values[index]
            })

            graph[equations[index][1]].append({
                "variable": equations[index][0],
                "value": 1/values[index]
            })
        
        # Loop through all queries
        def dfs(cur,curEdge,toFind) -> int:
            visited.add(cur)
            ans = -1
            # print('cur: {} and toFind: {}'.format(cur,toFind))
            for var in graph[cur]:
                if var["variable"] == toFind: ans = max(ans,curEdge*var["value"])
                elif var["variable"] in visited: continue
                else: ans = max(ans,dfs(var["variable"],curEdge*var["value"],toFind))
            return ans

        for query in queries:

            # Variable(s) don't exist in graph, so division is not valid
            if query[0] not in graph or query[1] not in graph:  
                result.append(-1)
                continue
            if query[0] in graph: 
                visited = set()
                result.append(dfs(query[0],1,query[1]))

        return result