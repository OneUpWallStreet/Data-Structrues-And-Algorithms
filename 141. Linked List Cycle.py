# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:


    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashset = set()

        while head != None:
            if head in hashset: return True
            else: hashset.add(head)
            head = head.next

        return False

    def constantMemoryhasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = (fast.next).next
            if slow == fast: return True

        return False
