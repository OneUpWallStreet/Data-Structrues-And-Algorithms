# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        def dfs(node,curSum):
            if node == None: return False

            curSum += node.val

            if not node.left and not node.right and curSum == targetSum: return True
            elif node.left and node.right: return dfs(node.left,curSum) or dfs(node.right,curSum)
            elif node.left: return dfs(node.left,curSum)
            elif node.right: return dfs(node.right,curSum)

        return dfs(root,0)