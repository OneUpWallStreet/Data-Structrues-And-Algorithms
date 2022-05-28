#include <iostream>
using namespace std;


struct KeyValuePair {
    int key;
    int value;
};



struct Node {
    KeyValuePair keyValuePair;
    Node* next;
    Node() :  next(nullptr) {
        keyValuePair.key = -1;
        keyValuePair.value = -1;
    }
    Node(KeyValuePair keyValuePair): keyValuePair(keyValuePair), next(nullptr) {}
};

class LinkedList {

    public:
        LinkedList(){
        }

    private:
        Node* head = new Node();
        int size = 0;
    
        void printAllElements(){
            Node* cur = head;
            int index = 0;

            while(true){
                cout << "\n" << endl;
                cout << "Index: " << index << endl;
                cout << "Key: " << cur->keyValuePair.key << endl;
                cout << "Value: " << cur->keyValuePair.value << endl;
                cout << "\n" << endl;

                if(cur->next==nullptr){
                    break;
                }
                cur = cur->next;
                index++;
            }
            return;
        }


    public: 

        int get(int key){
            Node* cur = head;
            while(true){
                if(cur->keyValuePair.key == key){
                    return cur->keyValuePair.value;
                }
                if(cur->next==nullptr){
                    break;
                }
                cur = cur->next;
            }
            return -1;

        }

        void deleteValue(int key){

            if(size==1){
                head = new Node();
                size--;
                return;
            }

            if(head->keyValuePair.key == key){
                head = head->next;
                size--;
                return;
            }

            Node* cur = head;

            while(cur->next != nullptr){
                if(cur->next->keyValuePair.key == key){
                    cur->next = cur->next->next;
                    size--;
                    return;
                }          
                // if(cur->next == nullptr){
                //     break;
                // }  
                cur = cur->next;
            }

            return;
        }

        bool doesValueExist(int key){
            Node* cur = head;
            while(true){
                if(cur->keyValuePair.key == key){
                    return true;
                }
                if(cur->next == nullptr){
                    break;
                }
                cur = cur->next;
            }
            return false;        
        }

        void updateValue(KeyValuePair keyValuePair){
            
            Node* cur = head;

            while(true){
                if(cur->keyValuePair.key == keyValuePair.key){
                    cur->keyValuePair.value = keyValuePair.value;
                    return;
                }

                if(cur->next == nullptr){
                    break;
                }

                cur = cur->next;
            }
            return;
        }

        void insert(KeyValuePair keyValuePair){

            Node* cur = head;

            if(size==0){
                cur->keyValuePair = keyValuePair;
                size++;
                return;
            }

            bool doesValueExist =  this->doesValueExist(keyValuePair.key);

            if(doesValueExist==true){

                cout << " IN does value exist" << endl;
                this->updateValue(keyValuePair);
                return;
            }
            

            while(cur->next!= nullptr){
                cur = cur->next;
            }

            Node* newNode = new Node(keyValuePair);

            cur->next = newNode;
            size++;
            return;

        }


};

struct SingleBucketEntity {
    LinkedList linkedList;
    // KeyValuePair allValues [100];
};

class MyHashMap {
    public:
        MyHashMap() {
            
        }
        
        void put(int key, int value) {
            int hashedValue = hashFunction(key);
            struct KeyValuePair keyValuePair = {key,value};
            buckets[hashedValue].linkedList.insert(keyValuePair);      
            return;      
        }
        
        int get(int key) {
            int hashedValue = hashFunction(key);
            int value = buckets[hashedValue].linkedList.get(key);
            return value;
        }
        
        void remove(int key) {
            int hashedValue = hashFunction(key);
            buckets[hashedValue].linkedList.deleteValue(key);
            return;
        }

    private:

        SingleBucketEntity buckets [1000];

        int hashFunction(int input){
            int key = input % 1000;
            return key;
        }


};


int main(){
    MyHashMap* hashMap = new MyHashMap();
    hashMap->put(8792,23484);
    hashMap->remove(8792); 
    int val = hashMap->get(8792);
    delete hashMap;
}
