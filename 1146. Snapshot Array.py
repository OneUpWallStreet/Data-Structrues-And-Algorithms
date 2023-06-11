class ListNode:
    def __init__(self,val = None, next = None,snap_id = None):
        self.val = val
        self.next = next
        self.snap_id = snap_id

class SnapshotArray:

    def __init__(self, length: int):
        self.array = [None]*length
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        if self.array[index] == None: self.array[index] = ListNode(val=val,next=None,snap_id=self.snap_id)
        
        cur = self.array[index]
        
        while cur:
            if cur.snap_id == self.snap_id: 
                cur.val = val
                return             
            elif cur.next == None: cur.next = ListNode(val = val,next = None,snap_id = self.snap_id)
            else: cur = cur.next

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:

        cur = self.array[index]
        hashmap = dict()
        maxKey = None

        while cur:
            if cur.snap_id == snap_id: 
                return cur.val
            hashmap[cur.snap_id] = cur.val
            cur = cur.next

        for key in hashmap.keys():
            if key < snap_id:
                if maxKey == None: maxKey = key
                else: maxKey = max(maxKey,key)

        if maxKey != None: return hashmap[maxKey]

        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)