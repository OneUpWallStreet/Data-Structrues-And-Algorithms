class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
       next = null;
    }
}


class Solution {
  public ListNode detectCycle(ListNode head) {

      ListNode tortoise = head;
      ListNode hare = head;

      ListNode intersectionNode = null;

      while(tortoise != null && hare != null && hare.next != null){
          tortoise = tortoise.next;
          hare = hare.next.next;
          if(tortoise==hare){
              intersectionNode = tortoise;
              break;
          }
      }

//      Found cycle, now let's find start node
      if(intersectionNode!=null){
          hare = head;
          while(hare!=intersectionNode){
              hare = hare.next;
              intersectionNode = intersectionNode.next;
          }
          return hare;
      }
      return null;
  }
}
