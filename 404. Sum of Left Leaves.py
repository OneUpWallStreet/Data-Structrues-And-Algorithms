# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if node == None:
                return
            if node.left != None and node.left.left == None and node.left.right == None:
                result += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result