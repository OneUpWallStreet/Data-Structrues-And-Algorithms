#include<iostream>

using namespace std;

struct Node {
	int value;
    Node* next = NULL;
    Node(int val){
        this->value = val;
        this->next = NULL;
    }
};


class MyLinkedList {

public:

    Node* head = new Node(0);
    int size = 0;


    MyLinkedList() {
        
        // head->next = NULL;
    }
    
    int get(int index) {


        if(index>size-1){
            return -1;
        }

        Node* cur = head;

        for(int i=0;i<index;i++){
            cur = cur->next;
        }

        return cur->value;
    }

    
    void addAtHead(int val) {

        Node* cur = head;

        if(size==0){
            cur->value = val;
            size++;
            return;
        }

        Node* newHead = new Node(val);
        newHead->next = cur;
        head = newHead;
        size++;
    }
    
    void addAtTail(int val) {
        Node* cur = head;
       
       if(size==0){
           cur->value = val;
           size++;
           return;
       }
       
        while(cur->next != NULL){
            cur = cur->next;            
        }
        cur->next = new Node(val);
        size++;
        return;
    }
    
    void addAtIndex(int index, int val) {

        if(index>size){
            return;
        }

        if(index == size){
            addAtTail(val);
            return;
        }

        if(index == 0){
            addAtHead(val);
            return;
        }

        Node* cur = head;
        

        for(int i=0;i<index-1;i++){
            cur = cur->next;
        }

        // cout << "Current value is" << cur->value << endl;


        Node* newNode = new Node(val);

        newNode->next = cur->next;
        cur->next = newNode;
        size++;
        return;

        
    }



    
    void deleteAtIndex(int index) {

        if(index>size-1 || size == 0){
            return;
        }

        Node* cur = head;

        if(index==0){
            if(size==1){
                cur = new Node(0);
                size--;
                return;
            }

            head = cur->next;
            size--;
            return;
        }

        Node* preCur = head;

        for(int i=0;i<index;i++){
            preCur = cur;
            cur = cur->next;            
        }

        preCur->next = cur->next;
        size--;

        
    }

	void printLinkedList() {

        Node* cur = head;

        while(true){
            cout << "value: " << cur->value << endl;

            if(cur->next == NULL){
                return;
            }

            cur = cur->next;
        }
	}
};

int main() {

	MyLinkedList* obj = new MyLinkedList();
	return 0;
}

