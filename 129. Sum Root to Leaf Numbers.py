# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node,cur):
            nonlocal result
            cur += str(node.val)
            if node.left != None:
                dfs(node.left,cur)
            if node.right != None:
                dfs(node.right,cur)
            if node.left == None and node.right == None:
                result += int(cur)
        dfs(root,"")
        return result