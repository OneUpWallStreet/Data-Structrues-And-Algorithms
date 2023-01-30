# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def dfs(node,array):
            if node == None:
                return
            elif node.left == None and node.right == None:
                array.append(node.val)
            dfs(node.left,array)
            dfs(node.right,array)

        arr1 = []
        arr2 = []

        dfs(root1,arr1)
        dfs(root2,arr2)
        
        if len(arr1) != len(arr2):
            return False
        
        for index in range(len(arr1)):
            if arr1[index] != arr2[index]:
                return False
                
        return True
