# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def depth(node,curDepth) -> int:
            if node == None:
                return curDepth
            curDepth += 1
            return max(depth(node.left,curDepth),depth(node.right,curDepth))
        def dfs(node):
            nonlocal result
            if node == None:
                return
            leftDepth = depth(node.left,0)
            rightDepth = depth(node.right,0)
            result = max(depth(node.left,0)+depth(node.right,0),result)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return result
        