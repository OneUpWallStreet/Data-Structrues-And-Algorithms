# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        hm = collections.defaultdict(int)

        def dfs(node,level):
            if node == None: return
            hm[level] += node.val
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        dfs(root,1)

        vals = [None, float('-inf')]
        for k,v in hm.items():
            if v > vals[1]:
                vals[0] = k
                vals[1] = v
        
        return vals[0]