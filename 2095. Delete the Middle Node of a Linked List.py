# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, head
        n = 0
        cur = head

        while cur != None:
            cur = cur.next
            n += 1
        
        mid = floor(n/2)

        counter = 0

        while counter != mid:
            p1 = p1.next
            p2 = p2.next
            counter += 1
        
        p1.next = p2.next   
        return dummy.next

