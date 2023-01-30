# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            nonlocal result
            if node == None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result