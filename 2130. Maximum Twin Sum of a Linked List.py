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


    # Code is not the best, but it works. Its Linear Time & Constant Space
    # Came up with this solution on my own
    def LinearTimeConstantSpacepairSum(self, head: Optional[ListNode]) -> int:
        
        listSize = 0 
        cur = head

        while cur != None:
            cur = cur.next
            listSize += 1
        
        mid = int(listSize/2)
        cur = head
        n = 0

        while n != mid:
            cur = cur.next
            n += 1

        # Reverse List
        prev = None
        
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        result = float('-inf')
        cur = head
        counter = 0

        while counter != mid:
            result = max(result,prev.val + cur.val)
            prev = prev.next
            cur = cur.next
            counter += 1


        return result