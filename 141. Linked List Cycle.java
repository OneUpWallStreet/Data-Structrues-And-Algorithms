import java.util.Set;
import java.util.HashSet;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}


class Solution {

    private Set<ListNode> set = new HashSet<>();

    public boolean hasCycle(ListNode head) {

        if(head==null){
            return  false;
        }
        else if (head.next == null){
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while(true){

            if(slow == fast){
                return true;
            }
            if(fast.next == null || fast.next.next == null){
                return  false;
            }

            slow = slow.next;
            fast = fast.next.next;

            
        }
  }
}
