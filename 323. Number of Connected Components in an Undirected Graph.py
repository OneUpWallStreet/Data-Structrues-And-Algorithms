
import collections


def unionFindSolution(n: int, edges: list) -> int:

    parents = [i for i in range(n)]
    rank = [1]*n

    # This will find the parent in forest
    def find(n):
        res = n
        while res != parents[res]:
            res = parents[res]        
        return res

    def union(n1,n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2: return 0

        if rank[p1] > rank[p2]:
            rank[p1] += rank[p2]
            parents[p2] = p1
        else:
            rank[p2] += rank[p1]
            parents[p1] = p2
        return 1
    
    result = n
    for n1,n2 in edges: result -= union(n1,n2)
    return result


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

# n = 5
# edges = [[0,1],[1,2],[3,4]]

# n = 6
# edges = [[0,1], [1,2], [2, 3], [4, 5]]


# n = 3
# edges = [[0,1], [0,2]]

n = 5
edges = [[0, 1], [1, 2], [2, 0], [3, 4]]

# print('There are {} components'.format(solution(n,edges)))
print('There are {} components'.format(unionFindSolution(n,edges)))