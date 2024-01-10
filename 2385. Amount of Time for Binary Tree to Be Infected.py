# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph = collections.defaultdict(list)

        def dfs(node):
            if not node: return
            if node.left: 
                graph[node.val].append(node.left.val)
                graph[node.left.val] = [node.val]
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val] = [node.val]
                dfs(node.right)
        
        dfs(root)

        q = collections.deque()

        q.append(start)
        visited = set()
        time = 0

        while q:
            
            for _ in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for nextNode in graph[cur]:
                    if nextNode not in visited:
                        q.append(nextNode)
            
            time += 1
                
        
        # print(time)
        return time -1 