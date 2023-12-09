# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        result = ""

        def dfs(node):
            nonlocal result
            if node == None: return
            result += str(node.val)
            if not node.left and not node.right: return
            if node.left or node.right: 
                result += "("
                dfs(node.left)
                result += ")"
            if node.right: 
                result += "("
                dfs(node.right)
                result += ")"
        
        dfs(root)
        return result