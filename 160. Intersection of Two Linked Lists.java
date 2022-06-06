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

    // O(m+n) Time & Space Space Compleixty

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


    // Code below is for solution, which runs in O(m+n) time complexity
    // & constant memory i.e. O(1)

    private int countLinkedListLength(ListNode head){
        int counter  = 0;
        ListNode cur = head;
        while(cur!=null){
            counter++;
            cur = cur.next;
        }
        return counter;
    }

    private ListNode returnAdjustedHead(ListNode head, int n){
        ListNode cur = head;
        while(n!=0 && cur!=null){
            n--;
            cur = cur.next;
        }
        return  cur;
    }


    public ListNode getIntersectionNodeConstantMemory(ListNode headA, ListNode headB) {

        ListNode inter = null;
        int lA = countLinkedListLength(headA);
        int lB = countLinkedListLength(headB);

        ListNode curA = headA;
        ListNode curB = headB;

        if(lA>lB){
            curA = returnAdjustedHead(headA,lA-lB);
        } else if (lB>lA) {
            curB = returnAdjustedHead(headB,lB-lA);
        }


        while (curA!=null && curB!=null){
            if(curA==curB){
                inter = curA;
                break;
            }
            curA = curA.next;
            curB = curB.next;
        }

        return inter;

    }
}