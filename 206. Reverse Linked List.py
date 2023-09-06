class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = p1
            p1 = cur
            cur = temp

        return p1        

