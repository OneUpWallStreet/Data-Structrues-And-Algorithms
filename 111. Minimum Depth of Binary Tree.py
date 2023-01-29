# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        result = sys.maxsize
        def dfs(node,pathLen):
            nonlocal result
            if node == None:
                return
            elif node.left == None and node.right == None:
                result = min(result,pathLen)
                return 
            pathLen += 1
            dfs(node.left,pathLen)
            dfs(node.right,pathLen)
        dfs(root,1)
        if root == None:
            return 0
        else:
            return result