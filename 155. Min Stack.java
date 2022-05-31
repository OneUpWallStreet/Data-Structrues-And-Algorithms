import java.util.*;

class MinStack {

    private ArrayList<Integer> array = new ArrayList<>();
    private PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();

    public MinStack() { }

    public void push(int val) {
        minHeap.add(val);
        array.add(val);
    }

    public void pop() {
        if(array.isEmpty()){
            return;
        }
        minHeap.remove(top());
        array.remove(array.size()-1);
    }

    public int top() {
        return array.get(array.size()-1);
    }

    public int getMin() {
        return minHeap.peek();
    }
}