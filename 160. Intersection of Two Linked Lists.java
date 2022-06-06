import java.util.Stack;

class ListNode {
      int val;
      ListNode next;
      ListNode(int x) {
          val = x;
          next = null;
      }
}

class Solution {

    private Stack<ListNode> s1 = new Stack<>();
    private Stack<ListNode> s2=  new Stack<>();


    private void fillStack(ListNode head, Stack<ListNode> stack){
        ListNode cur = head;
        while(cur!=null){
            stack.push(cur);
            cur = cur.next;
        }
    }


    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        ListNode inter = null;

        fillStack(headA,s1);
        fillStack(headB,s2);

        while (!s1.isEmpty() && !s2.isEmpty()){
            if(s1.peek() == s2.peek()){
                inter = s1.peek();
            }
            s1.pop();
            s2.pop();
        }
        return inter;
    }
}