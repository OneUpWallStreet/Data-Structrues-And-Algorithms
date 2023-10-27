class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []

        # L - N - R
        def dfs(node):
            if node == None: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k-1]

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        
        s = collections.deque()
        cur = root

        while s or cur:

            while cur:
                s.append(cur)
                cur = cur.left
            
            cur = s.pop()
            k -= 1
            if k == 0: return cur.val
            cur = cur.right
