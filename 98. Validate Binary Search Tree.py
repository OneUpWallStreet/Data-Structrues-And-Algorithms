# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, leftCeiling, rightFloor):
            if node == None: return True
            elif node.val >= leftCeiling or node.val <= rightFloor: return False
            return dfs(node.left,node.val,rightFloor) and dfs(node.right,leftCeiling,node.val)
        
        return dfs(root,float('inf'),float('-inf'))
        