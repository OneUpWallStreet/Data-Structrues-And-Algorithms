
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node == None: return None

        hashmap, visited = dict(), set()

        def initNewNodes(n):
            hashmap[n] = Node(n.val)
            for nextNode in n.neighbors:
                if nextNode not in hashmap:
                    initNewNodes(nextNode)

        def addNeighbors(n):

            visited.add(n.val)

            for nextNode in n.neighbors:
                hashmap[n].neighbors.append(hashmap[nextNode])
                if nextNode.val not in visited: 
                    addNeighbors(nextNode)
        

        initNewNodes(node)
        addNeighbors(node)

        return hashmap[node]