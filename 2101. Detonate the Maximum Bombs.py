class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        result, counter = -sys.maxsize, 0
        visited = set()

        for b1 in range(len(bombs)):
            x1, y1, r1 = bombs[b1]
            for b2 in range(len(bombs)):
                if b2 == b1:
                    continue
                x2, y2, r2 = bombs[b2]
                if (pow(x1-x2,2)+pow(y1-y2,2) <= pow(r1,2)): graph[b1].append(b2)
        
        def dfs(bomb):
            nonlocal result,counter
            counter += 1
            visited.add(bomb)
            for nextbomb in graph[bomb]:
                if nextbomb not in visited:
                    dfs(nextbomb)
                

        for index in range(len(bombs)):
            counter = 0
            dfs(index)
            visited = set()
            result = max(result,counter)

        return result