#include<iostream>
#include<vector>

using namespace std;

class MinHeap {

    public:
        
        MinHeap(){

        }

        int peek(){
            return items[0];
        }

        int poll() {
            int item = items[0];
            items[0] = items[size-1];
            size--;
            heapifyDown();
            return item;
        }

        void add(int item){
            items[size] = item;
            size++;
            hepifyUp();
        }

        void hepifyUp(){

            int index = size-1;
            
            while(hasParent(index) && parent(index) > items[index]){
                swapValues(getParentIndex(index),index);
                index = getParentIndex(index);
            }

        }

        void heapifyDown(){

            int index = 0;

            while(hasLeftChild(index)){
                int smallerChildIndex = getLeftChildIndex(index);
                if(hasRightChild(index) && rightChild(index) < leftChild(index)){
                    smallerChildIndex = getRightChildIndex(index);
                }

                if(items[index]<items[smallerChildIndex]){
                    break;
                }
                else{
                    swap(index,smallerChildIndex);
                }

                index  = smallerChildIndex; 
            }

        }

    private:
        int size = 0;
        vector<int> items;

        int getLeftChildIndex(int parentIndex){
            return (2 * parentIndex) + 1;
        }

        int getRightChildIndex(int parentIndex){
            return (2 * parentIndex) + 2;
        }

        int getParentIndex(int childIndex){
            return (childIndex-1)/2;
        }

        bool hasLeftChild(int index){
            return getLeftChildIndex(index) < size;
        }

        bool hasRightChild(int index){
            return getRightChildIndex(index) < size;
        }

        bool hasParent(int index){
            return getParentIndex(index) >= 0;
        }

        int leftChild(int index){
            return items[getLeftChildIndex(index)];
        }

        int rightChild(int index){
            return items[getRightChildIndex(index)];
        }

        int parent(int index){
            return items[getParentIndex(index)];
        }

        void swapValues(int firstIndex, int secondIndex){
            int temp = items[firstIndex];
            items[firstIndex] = items[secondIndex];
            items[secondIndex] = temp;
        }



};

