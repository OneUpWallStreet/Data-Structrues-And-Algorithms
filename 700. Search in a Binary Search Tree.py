class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None or root.val == val: return root
        left = self.searchBST(root.left,val)
        return left if left != None else self.searchBST(root.right,val)