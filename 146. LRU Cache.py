class Node:
    def __init__(self,key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = dict()
        self.Left, self.Right = Node(), Node()
        self.Left.next = self.Right
        self.Right.prev = self.Left
        
    def remove(self,node): 
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self,node): 
        prev = self.Right.prev
        prev.next = node
        node.next = self.Right
        node.prev = prev
        self.Right.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.hm: return -1
        self.remove(self.hm[key])
        self.insert(self.hm[key])
        return self.hm[key].val        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hm: self.remove(self.hm[key])

        self.hm[key] = Node(key,value)
        self.insert(self.hm[key])

        if len(self.hm) > self.capacity:
            lru = self.Left.next
            self.remove(lru)
            del self.hm[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)