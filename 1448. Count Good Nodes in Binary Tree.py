# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Traverse through all paths
            # Store max value in path and compare it
        res = 0
        def dfs(node,maxVal): 
            nonlocal res
            if node == None: return
            elif maxVal <= node.val:
                res += 1
            maxVal = max(maxVal,node.val)
            dfs(node.left,maxVal)
            dfs(node.right,maxVal)

        dfs(root,float('-inf'))
        return res