# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        arr = []
        cur = head

        while cur != None:
            arr.append(cur)
            cur = cur.next

        p1, p2 = 0, len(arr) - 1

        while p1 < p2:
            arr[p1].next = arr[p2]
            p1 += 1
            if p1 == p2: break
            arr[p2].next = arr[p1]
            p2 -= 1
        arr[p2].next = None

        
