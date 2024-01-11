# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        result = float('-inf')

        def dfs(node, maxVal, minVal):
            nonlocal result
            if node == None: return
            maxVal = max(maxVal,node.val)
            minVal = min(minVal,node.val)
            result = max(result, abs(minVal-maxVal))
            dfs(node.left,maxVal,minVal)
            dfs(node.right,maxVal,minVal)
        dfs(root,root.val,root.val)

        return result
        