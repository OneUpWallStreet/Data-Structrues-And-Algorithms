import java.util.HashMap;
import java.util.Random;


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 

class Solution {

    int size;
    HashMap<Integer,Integer> map = new HashMap<>();
    Random random = new Random();

    public Solution(ListNode head) {
        ListNode cur = head;
        size = 0;
        while(cur!=null){
            size++;
            map.put(size,cur.val);
            cur = cur.next;
        }
    }

    public int getRandom() {
        int key = random.nextInt(size - 1 + 1) + 1;
        return map.get(key);
    }
}