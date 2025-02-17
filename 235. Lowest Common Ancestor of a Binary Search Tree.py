# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Time complexity: O(logN) because we use recursion according to the BST property
    def lowestCommonAncestorLogNSolution(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val: return root
        if root.val < p.val and root.val < q.val:  return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > p.val and root.val > q.val: return self.lowestCommonAncestor(root.left,p,q)
        else: return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None: return None
        if root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        return left if left != None else right
