# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        t1, t2 = [], []

        def dfs(node, first):
            
            if node == None: return
            elif node.left == None and node.right == None: 
                if first: t1.append(node.val)
                else: t2.append(node.val)
            dfs(node.left,first)
            dfs(node.right,first)
        
        dfs(root1,True)
        dfs(root2,False)

        return t1 == t2
