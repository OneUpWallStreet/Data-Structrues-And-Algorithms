# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot) -> bool:
            if root == None and subRoot == None: return True
            elif root == None or subRoot == None: return False
            elif root.val != subRoot.val: return False
            return dfs(root.left,subRoot.left) and dfs(root.right,subRoot.right)

        s = collections.deque()
        s.append(root)
        while s:
            cur = s.pop()
            if cur == None: continue
            if cur.val == subRoot.val: 
                if dfs(cur,subRoot): return True
            s.append(cur.left)
            s.append(cur.right)
            
        return False