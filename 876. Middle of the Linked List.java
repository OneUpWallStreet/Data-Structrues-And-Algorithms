import java.util.Stack;

// * Definition for singly-linked list.
class ListNode {
     int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {

    Stack<ListNode> stack = new Stack<>();

    public ListNode middleNode(ListNode head) {

        ListNode cur = head;

        while(cur!=null){
            stack.add(cur);
            cur = cur.next;
        }

        int middle = stack.size()/2;

        while(stack.size()>middle+1){
            stack.pop();
        }


        return stack.peek();
    }
}