# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,minVal,maxVal) -> bool:
            if node == None: return True
            elif node.val >= maxVal or node.val <= minVal: return False
            elif node.left == None: return dfs(node.right,node.val,maxVal)
            elif node.right == None: return dfs(node.left,minVal,node.val)
            else: return dfs(node.right,node.val,maxVal) and dfs(node.left,minVal,node.val)

        return dfs(root,float('-inf'),float('inf'))




