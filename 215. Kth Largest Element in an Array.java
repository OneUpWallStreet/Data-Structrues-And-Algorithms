import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
    public int findKthLargest(int[] nums, int k) {
        for(int num: nums){
            heap.add(num);
        }
        for(int i=0;i<k-1;i++){
            heap.poll();
        }
        return heap.peek();
    }
}