# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1: 
            cur = TreeNode(val)
            cur.left = root
            return cur

        def dfs(node,cur):
            if node == None: return
            if cur+1 == depth:
                left = node.left if node.left else None
                right = node.right if node.right else None
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = left
                node.right.right = right
                return               
            dfs(node.right,cur+1)
            dfs(node.left,cur+1)

        dfs(root,1)
        return root