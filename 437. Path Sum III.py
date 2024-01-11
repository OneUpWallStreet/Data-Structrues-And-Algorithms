# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        result = 0

        def dfs(node,curSum):
            nonlocal result
            if node == None: return

            curSum += node.val
            if curSum == targetSum: result += 1

            if node.left: dfs(node.left,curSum)
            if node.right: dfs(node.right, curSum)


        def newPath(node):
            if node == None: return

            dfs(node,0)

            newPath(node.left)
            newPath(node.right)

            
        newPath(root)    
        return result