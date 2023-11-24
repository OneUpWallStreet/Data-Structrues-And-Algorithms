from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Better Solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        targetSum -= root.val
        if root.left == None and root.right == None and targetSum == 0: return True 
        if root.left != None:
            if self.hasPathSum(root.left,targetSum): return True
        if root.right != None:
            if self.hasPathSum(root.right,targetSum): return True
        return False

