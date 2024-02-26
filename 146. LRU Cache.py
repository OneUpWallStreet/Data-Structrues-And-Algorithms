class Node:
    def __init__(self,key = 0,val = 0):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = dict()
        self.capacity = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert(self,node): 
        prev,nextN = self.right.prev, self.right
        prev.next, nextN.prev = node, node
        node.prev, node.next = prev, nextN


    def remove(self,node):         
        prev, nextN = node.prev, node.next
        prev.next = nextN
        nextN.prev = prev


    def get(self, key: int) -> int:
        if key in self.hm: 
            # modify recently used
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm: self.remove(self.hm[key])

        self.hm[key] = Node(key,value)
        self.insert(self.hm[key])
        print(len(self.hm),self.capacity)
        if len(self.hm) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hm[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)