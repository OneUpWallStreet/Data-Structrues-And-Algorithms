#include <iostream>

using namespace std;
#define MAX_COUNT 1000000

class MyHashSet {

    public:

        MyHashSet() {
            fill_n(buckets,MAX_COUNT,-1);            
        }

        void add(int key) {
            int hashedValue = hashFunction(key);
            buckets[hashedValue] = key;
            return;
        }
        
        void remove(int key) {
            int hashedValue = hashFunction(key);
            buckets[hashedValue] = -1;
            return;
        }
        
        bool contains(int key) {
            int hashedValue = hashFunction(key);
            if(buckets[hashedValue]==-1){
                return false;
            }   
            else{
                return true;
            }
        }

    private:

        int buckets[MAX_COUNT];

        int hashFunction(int input){
            int key = input % MAX_COUNT;
            return key;
        }


};


int main(){
    MyHashSet* hashSet = new MyHashSet();
    hashSet->add(8792);
    hashSet->contains(8792);
    hashSet->remove(8792);
    delete hashSet;
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */