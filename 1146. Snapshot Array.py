class SnapshotArray:

    def __init__(self, length: int):
        self.hashmap = defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index in self.hashmap and len(self.hashmap[index]) >0 and self.hashmap[index][-1][0] == self.snap_id:
            self.hashmap[index][-1][1] = val
            return
        self.hashmap[index].append([self.snap_id,val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        values = self.hashmap[index]
        left, right = 0, len(values)-1
        res = -1
        while left <= right:
            mid = left + (right-left)//2
            if values[mid][0] <= snap_id:
                res = mid
                left = mid + 1            
            else: right = mid - 1

        if res == -1: return 0
        return values[res][1]


# LinkedList Solution gets TLE :(

# class ListNode:
#     def __init__(self,val = None, next = None,snap_id = None):
#         self.val = val
#         self.next = next
#         self.snap_id = snap_id

# class SnapshotArray:

#     def __init__(self, length: int):
#         self.array = [None]*length
#         self.snap_id = 0
        
#     def set(self, index: int, val: int) -> None:
#         if self.array[index] == None: self.array[index] = ListNode(val=val,next=None,snap_id=self.snap_id)
        
#         cur = self.array[index]
        
#         while cur:
#             if cur.snap_id == self.snap_id: 
#                 cur.val = val
#                 return             
#             elif cur.next == None: cur.next = ListNode(val = val,next = None,snap_id = self.snap_id)
#             else: cur = cur.next

#     def snap(self) -> int:
#         self.snap_id += 1
#         return self.snap_id - 1

#     def get(self, index: int, snap_id: int) -> int:

#         cur = self.array[index]
#         hashmap = dict()
#         maxKey = None

#         while cur:
#             if cur.snap_id == snap_id: 
#                 return cur.val
#             hashmap[cur.snap_id] = cur.val
#             cur = cur.next

#         for key in hashmap.keys():
#             if key < snap_id:
#                 if maxKey == None: maxKey = key
#                 else: maxKey = max(maxKey,key)

#         if maxKey != None: return hashmap[maxKey]

#         return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)