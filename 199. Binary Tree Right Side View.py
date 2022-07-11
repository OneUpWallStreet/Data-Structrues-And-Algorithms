import collections

class Solution:
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