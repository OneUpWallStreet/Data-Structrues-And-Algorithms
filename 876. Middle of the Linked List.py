# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count, cur = 0, head

        while cur != None:
            cur = cur.next
            count += 1
        mid = (count // 2) 
        while mid > 0:
            head = head.next
            mid -= 1

        return head

        