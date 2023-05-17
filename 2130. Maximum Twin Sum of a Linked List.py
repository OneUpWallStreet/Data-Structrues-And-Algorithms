# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        stack = collections.deque()
        result = -sys.maxsize
        cur = head

        # Create Stack
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        
        while head != None:
            result = max(result,head.val+stack.pop())
            head = head.next

        return result



