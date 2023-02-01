# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = sys.maxsize
        prevNode = None
        def dfs(node):
            nonlocal result,prevNode
            if node == None:
                return
            dfs(node.left)
            if prevNode != None:
                result = min(result,abs(node.val-prevNode))
            prevNode = node.val
            dfs(node.right)
        dfs(root)
        return result
