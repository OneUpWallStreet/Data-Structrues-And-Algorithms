# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        result = sys.maxsize
        prevVal = None

        def dfs(node):
            nonlocal result,prevVal
            if node == None:
                return
            dfs(node.left)
            if prevVal != None:
                result = min(result,abs(node.val-prevVal))  

            prevVal = node.val  
            dfs(node.right)
        
        dfs(root)
        return result        


