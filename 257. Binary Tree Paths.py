# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node,cur):
            nonlocal result
            if len(cur) == 0:
                cur += str(node.val)
            else:
                cur += "->" + str(node.val)
            if node.left != None:
                dfs(node.left,cur)
            if node.right != None:
                dfs(node.right,cur)
            if node.left == None and node.right == None:
                result.append(cur)
        dfs(root,"")
        return result