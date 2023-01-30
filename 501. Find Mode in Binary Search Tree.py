# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        heap = []
        result = []
        maxNumber = -1
        heapq.heapify(heap)
        hashmap = defaultdict(int)
        
        def dfs(node):
            
            if node == None:
                return

            hashmap[node.val] += 1
            heapq.heappush(heap,[-1*hashmap[node.val],node.val])
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        freq,num = heapq.heappop(heap)
        maxNumber = freq*-1
        result.append(num)

        while heap:
            freq,num = heapq.heappop(heap)
            if (-1*freq) == maxNumber:
                result.append(num)
            
        return result