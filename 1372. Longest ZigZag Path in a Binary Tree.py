# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        result = 0

        def dfs(node, direction, curLen):
            nonlocal result

            if node == None: return

            curLen += 1
            result = max(result, curLen)  

            if direction == 'left':
                dfs(node.right,'right',curLen)
                dfs(node.left,'left',1)
            else:
                dfs(node.left,'left',curLen)
                dfs(node.right,'right',1)

        dfs(root,'left',0)
        dfs(root,'right',0)
        return result - 1

