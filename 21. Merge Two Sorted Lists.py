# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        result = None

        def addNode(val: int):
            nonlocal head,result
            if head == None: 
                head = ListNode(val)
                result = head
            else:
                head.next = ListNode(val)
                head = head.next

        while list1 != None and list2 != None:
            
            if list1.val == list2.val:
                addNode(list1.val)
                addNode(list2.val)
                list1 = list1.next
                list2 = list2.next
            elif list1.val < list2.val:
                addNode(list1.val)
                list1 = list1.next
            else:
                addNode(list2.val)
                list2 = list2.next

        while list1 != None:
            addNode(list1.val)
            list1 = list1.next

        while list2 != None:
            addNode(list2.val)
            list2 = list2.next
        
        return result