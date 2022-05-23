import java.util.Set;
import java.util.HashSet;

class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

class Solution {

    public void printLinkedList(ListNode head){
        ListNode cur = head;
        while(cur != null){
            System.out.println("Value: "+cur.val);
            cur = cur.next;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {

        ListNode cur = head;
        ListNode prev = null;

        Set<Integer> set = new HashSet<Integer>();

        while(cur != null){
            if(set.contains(cur.val)){
                prev.next = cur.next;
                cur = cur.next;
                continue;
            }
            set.add(cur.val);
            prev = cur;
            cur = cur.next;
        }

        return head;
    }

}
