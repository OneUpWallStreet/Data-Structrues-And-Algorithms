import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def BFSLevelOrderRightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = []
        q = collections.deque()

        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur: continue
                level.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if len(level) > 0: levels.append(level)

        return [level[-1] for level in levels]




    def BetterDFSRightSideView(self, root: Optional[TreeNode]) -> List[int]:

        depth = 0
        levels = collections.defaultdict(list)
        res = []

        def dfs(node,curLevel):
            nonlocal depth
            if node == None: return
            levels[curLevel].append(node.val)
            curLevel += 1
            depth = max(depth,curLevel)
            dfs(node.left,curLevel)
            dfs(node.right,curLevel)

        dfs(root,0)

        for i in range(depth): res.append(levels[i][-1])
        return res

#   This is from July 2022
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = collections.defaultdict(list)
        
        depth = 0
        result = []
        
        def dfs(node,currentLevel):
            nonlocal levels,result,depth
            if node == None:
                return
            levels[currentLevel].append(node.val)
            
            currentLevel += 1
            
            depth = max(depth,currentLevel)
            
            dfs(node.left,currentLevel)
            dfs(node.right,currentLevel)
                    
        
        dfs(root,0)
        
        for lev in range(depth):
            result.append(levels[lev].pop())
        
        return result