# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        result = 0

        def checkForPalindrome(hm):
            usedOne = False

            for k,v in hm.items():
                if v % 2 == 0: continue
                else:
                    if not usedOne: 
                        usedOne = True
                        continue
                    else: return False
            
            return True


        def dfs(node, hm):
            nonlocal result
            if node == None: return
            hm[node.val] += 1

            if node.left == None and node.right == None and checkForPalindrome(hm): result += 1

            dfs(node.left,hm)
            dfs(node.right,hm)

            hm[node.val] -= 1

        dfs(root,collections.defaultdict(int))
        return result