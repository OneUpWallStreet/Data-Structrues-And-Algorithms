#include<iostream>
#include<vector>
#include<queue>
using namespace std;

void printQueue(queue<int> q);




class MyStack {
    public:
        MyStack() {
           
        }
        
        void push(int x) {
           q.push(x);
        }
        
        int pop() {
            return 1;
        }
        
        int top() {
            return q.back();
        }
        
        bool empty() {
            if(q.size()==0){
                return true;
            }
            return false;
        }

    private: 
        queue<int> q;
        queue<int> q2;


};

void printQueue(queue<int> q){

    queue<int> g = q;
    while (!g.empty()) {
        cout << '\t' << g.front();
        g.pop();
    }
    cout << '\n';
}

int main(){

    MyStack stack;
    queue<int> q;

    q.push(10);
    q.push(15);
    q.push(100);

    printQueue(q);

    cout << q.back() << endl;

}