#include<iostream>
#include<algorithm>
using namespace std;

// Constraints:

//     1 <= k <= 1000
//     0 <= value <= 1000
//     At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.


// Solutions fails test case number -> 54 out of 58. Fix Later

class MyCircularQueue {

    public:

        MyCircularQueue(int k) {
            bufferSize = k;
            buffer = new int[k];
            fill_n(buffer,k,-1);
        }

        bool enQueue(int value) {

            if(isFull()==true){
                return false;
            }

            int nextFront = rotateNumber(front);

            buffer[nextFront] = value;
            front = nextFront;
            return true;

        }
        
        bool deQueue() {
            if(isEmpty()==true){
                return false;
            }
            buffer[rear] = -1;
            rear = rotateNumber(rear);
            return true;
        }
        
        int Rear() {
            if(front != -1){
                return buffer[front];
            }
            return -1;
        }
        
        int Front() {
            return buffer[rear];
        }
        
        bool isEmpty() {
            if(front==-1 || buffer[front] == -1 || buffer[rear] == -1){
                return true;
            }
            return false;    
        }
        
        bool isFull() {

            // printValues();
            // cout << " buffersize-1: " << bufferSize-1 << endl;
            // cout << "buffer[front]: " << buffer[front] << endl;

            if(rear==0 && front == bufferSize-1 && buffer[front] != -1){
                return true;
            }

            return false;
        }

        void printBuffer(){
            cout << "\n" << endl;

            for(int i=0;i<bufferSize;i++){
                cout <<  buffer[i] << endl;
            }

            cout << "\n" << endl;

        }

        void printValues() {
            cout << "Rear: " << rear << endl;
            cout << "Front: " << front << endl;
        }

    private:
        int *buffer;
        int bufferSize;
        int rear = 0;
        int front = -1;


        int rotateNumber(int number){
            // cout << "Number given is: " << number << endl;
            if(number==bufferSize-1){
                // cout << " I gave back 0" << endl;
                return 0;
            }
            else{
                int nextNumber = number+1;
                return nextNumber;
            }
        }

};

// ["MyCircularQueue","enQueue","Rear","Front","deQueue","Front","deQueue","Front","enQueue","enQueue","enQueue","enQueue"]
// [[3],[2],[],[],[],[],[],[],[4],[2],[2],[3]]

int main(){

    MyCircularQueue circularBuffer(3);
    circularBuffer.enQueue(2);
    circularBuffer.deQueue();
    circularBuffer.deQueue();

    circularBuffer.printValues();
    circularBuffer.printBuffer();

    // circularBuffer.enQueue(4);
    // circularBuffer.enQueue(2);
    // circularBuffer.enQueue(2);
    // circularBuffer.enQueue(3);



    // circularBuffer.enQueue(2);
    // circularBuffer.Rear();

    // circularBuffer.enQueue(1);
    // circularBuffer.enQueue(2);
    // circularBuffer.enQueue(3);
    // circularBuffer.enQueue(4);
    // // cout << "4 is: " <<  << endl;
    // cout << "Rear is: " << circularBuffer.Rear() << endl;

    // circularBuffer.printBuffer();


    // circularBuffer.enQueue(4);
    // circularBuffer.enQueue(2);
    // circularBuffer.enQueue(9);
    // circularBuffer.enQueue(7);
    // circularBuffer.enQueue(10);

    // circularBuffer.deQueue();
    // circularBuffer.deQueue();
    // circularBuffer.deQueue();
    // circularBuffer.deQueue();
    // circularBuffer.deQueue();

    // cout << "isEmpty: " << circularBuffer.isEmpty() << endl;
    // circularBuffer.printValues();

    // bool answer = circularBuffer.enQueue(10);

    // cout << "answer: " << answer << endl;


    // circularBuffer.printBuffer();

    // circularBuffer.printValues();
    


    // circularBuffer.enQueue(10000);

    // circularBuffer.deQueue();

    // circularBuffer.printBuffer();

    // cout << "\n Now DeQueing \n" << endl;

    // circularBuffer.deQueue();
    // circularBuffer.deQueue();
    // circularBuffer.enQueue(23484);


    // circularBuffer.printBuffer();

    // cout << "Rear is: " << circularBuffer.Rear() << endl;




    
    // cout << "Front: " << circularBuffer.Front() << endl;
    // cout << "Rear: " << circularBuffer.Rear() << endl;
    
    return 0;
}   