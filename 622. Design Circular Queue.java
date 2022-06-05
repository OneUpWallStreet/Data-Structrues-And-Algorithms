import java.util.LinkedList;


class MyCircularQueue {

    private LinkedList<Integer> data = new LinkedList<>();
    private int size;

    public MyCircularQueue(int k) {
        size  = k;
    }

    public boolean enQueue(int value) {
        if(data.size()==size){
            return false;
        }
        return data.add(value);
    }

    public boolean deQueue() {
        if(data.size()==0){
            return false;
        }

        data.pollFirst();
        return true;
    }

    public int Front() {
        if(data.size()==0){
            return -1;
        }
        return data.peekFirst();
    }

    public int Rear() {
        if(data.size()==0){
            return -1;
        }
        return data.peekLast();
    }

    public boolean isEmpty() {
        return data.size()==0;
    }

    public boolean isFull() {
        return data.size()==size;
    }
}