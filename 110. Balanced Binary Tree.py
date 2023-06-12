# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node,height) -> int:
            if node == None: return height
            else: return max(depth(node.left,height+1),depth(node.right,height+1))
            
        if root == None: return True
        elif abs(depth(root.left,0)-depth(root.right,0)) > 1: return False
        else: return self.isBalanced(root.right) and self.isBalanced(root.left)