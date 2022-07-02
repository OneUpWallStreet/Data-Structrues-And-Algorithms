from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = set()

        def dfs(node: int) -> bool:
            if arr[node] == 0:
                return True
            if node + arr[node] in range(len(arr)) and node + arr[node] not in visited and \
                node - arr[node] in range(len(arr)) and node - arr[node] not in visited:
                visited.add(node+arr[node])
                visited.add(node-arr[node])
                return dfs(node+arr[node]) or dfs(node-arr[node])
            elif node + arr[node] in range(len(arr)) and node + arr[node] not in visited:
                visited.add(node+arr[node])
                return dfs(node+arr[node])
            elif node - arr[node] in range(len(arr)) and node - arr[node] not in visited:
                visited.add(node-arr[node])
                return dfs(node-arr[node])
            return False

        visited.add(start)
        return dfs(start)
