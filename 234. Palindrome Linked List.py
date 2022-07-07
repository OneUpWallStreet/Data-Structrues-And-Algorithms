import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
                
        deq = collections.deque()
        
        cur = head
        while cur != None:
            deq.append(cur.val)
            cur = cur.next
            
        while len(deq) > 1:
            if deq.pop() != deq.popleft():
                return False
        
        return True
        