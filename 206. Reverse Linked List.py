class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        next = None
        prev = None
        
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev