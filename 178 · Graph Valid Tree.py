
import collections

def solution(n: int,edges: list):

    graph = collections.defaultdict(list)

    for edge in edges: 
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = set()

    def dfs(node,parent):
        if node in visited: return False
        visited.add(node)
        for nextNode in graph[node]:
            if nextNode == parent: continue
            if not dfs(nextNode,node): return False        
        return True

    return dfs(0,-1) and n == len(visited)


# Examples 
# Input: 
# n = 5 
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output 
# True


# Input: 
n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


print('The graph is valid answer: ',solution(n,edges))
