# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = collections.deque()
        q.append(root)
        levels = []

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == None: continue
                level.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            
            if level: levels.append(level)
        
        for i in range(len(levels)):
            level = levels[i]
            cur = None
    
            even = i%2 == 0
            for val in level:
                if even and val % 2 == 0: return False
                elif not even and val % 2 != 0:  return False
                elif cur and even and val <= cur:  return False
                elif cur and not even and val >= cur:  return False

                cur = val
                
        return True
        
