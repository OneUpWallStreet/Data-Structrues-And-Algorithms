# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == None: continue
                level.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if level: result.append(level)

        return result
