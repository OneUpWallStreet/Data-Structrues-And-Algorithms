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

          if(head == null){
              return false;
          }

          ListNode cur = head;

          while(true){

              if(set.contains(cur)){
                  return true;
              }

              set.add(cur);
              if(cur.next == null){
                  break;
              }
              cur = cur.next;
          }

        return false;
    }
}