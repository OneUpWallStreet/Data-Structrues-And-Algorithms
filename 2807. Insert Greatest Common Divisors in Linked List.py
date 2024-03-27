# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            gcd = ListNode(math.gcd(cur.val,cur.next.val))
            temp = cur.next
            cur.next = gcd
            gcd.next = temp
            cur = temp
        return head