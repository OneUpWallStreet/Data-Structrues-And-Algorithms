# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node,key):

            if node == None: return

            if key < node.val:  node.left = dfs(node.left,key)
            elif key > node.val:  node.right = dfs(node.right,key)
            
            else:
                if not node.left and not node.right: return None
                elif not node.left: return node.right
                elif not node.right: return node.left

                temp = minNode(node.right)
                node.val = temp.val
                node.right = dfs(node.right,temp.val)

            return node
                
        def minNode(node) -> int:
            cur = node
            while cur.left is not None: cur = cur.left
            return cur
            
        return dfs(root,key)