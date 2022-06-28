from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        intersection = None

        while slow != None and fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                intersection = slow
                break

        if intersection == None:
            return None

        slow = head

        while intersection != slow:
            slow = slow.next
            intersection = intersection.next

        return intersection

