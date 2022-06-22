public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}


class Solution {

    func reverseList(_ head: ListNode?) -> ListNode? {
        
        var prev: ListNode? = nil
        var next: ListNode? = nil
        var cur = head
        
        while cur != nil {
            next = cur!.next
            cur!.next = prev
            prev = cur
            cur = next
        }
            
        return prev
    }
}