class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        result = 0

        for index in range(len(manager)): 
            if manager[index] == -1: continue
            graph[manager[index]].append(index)
        
        def dfs(index,current):
            nonlocal result

            current += informTime[index]
            result = max(current,result)

            for nextNode in graph[index]:
                dfs(nextNode,current)
            
        dfs(headID,0)

        return result