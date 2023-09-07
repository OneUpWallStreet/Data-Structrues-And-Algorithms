# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        result = -1

        def depth(node,d):
            if node == None: return d
            d += 1
            return max(depth(node.left,d),depth(node.right,d))

        def dfs(node):
            nonlocal result
            if node == None: return
            result = max(result,depth(node.left,0)+depth(node.right,0))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
