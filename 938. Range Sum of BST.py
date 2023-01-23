# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if node == None:
                return 
            if node.val >= low and node.val <= high:
                result += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result