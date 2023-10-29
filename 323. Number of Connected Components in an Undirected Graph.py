
import collections

def solution(n: int, edges: list) -> int:
    
    graph = collections.defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = set()

    def dfs(node):

        visited.add(node)

        for nextNode in graph[node]:
            if nextNode not in visited:
                dfs(nextNode)
    
    result = 0

    for node in range(n):
        if node not in visited:
            result += 1
            dfs(node)
    
    return result

n = 5
edges = [[0,1],[1,2],[3,4]]

print('There are {} components'.format(solution(n,edges)))