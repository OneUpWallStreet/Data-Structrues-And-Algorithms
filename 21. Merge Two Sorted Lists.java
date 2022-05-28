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

      private ListNode result = new ListNode();
      private boolean isResultEmpty = true;

      public void addToResult(int value){

          if(isResultEmpty){
              result.val = value;
              isResultEmpty = false;
              return;
          }

          ListNode cur = result;

          while(cur.next != null){
              cur = cur.next;
          }
          ListNode newNode = new ListNode(value);

          cur.next = newNode;

      }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if(list1 == null){
            return  list2;
        }
        else if(list2 == null){
            return  list1;
        }
        else if(list1 == null && list2 == null){
            return list1;
        }

        while(list1 != null || list2 != null){

            if(list1 == null && list2 != null){
                addToResult(list2.val);
                list2 = list2.next;
                continue;
            }

            if(list2 == null && list1 != null){
                addToResult(list1.val);
                list1 = list1.next;
                continue;
            }


            if(list1 != null && list1.val <= list2.val){
                addToResult(list1.val);
                list1 = list1.next;
                continue;

            }


            if(list2 != null && list2.val <= list1.val){
                addToResult(list2.val);
                list2 = list2.next;
                continue;
            }
        }

        return result;
    }
}



