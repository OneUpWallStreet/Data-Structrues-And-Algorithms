#include<iostream>
using namespace std;

/**
 * Definition for singly-linked list.

 */
 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };


class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        
        ListNode* cur = head;
        ListNode* prev = NULL;
        ListNode* next = NULL;


        while(cur != NULL){
            next = cur->next;
            cur->next = prev;

            prev = cur;
            cur = next;
        }

        return prev;
    }


    void printLinkedList(ListNode* head){

        ListNode* cur = head;
        cout << "List-> ";
        while(true){
            cout << " " << cur->val << " ";
            if(cur->next == nullptr){
                break;
            }
            cur = cur->next;
        }
        cout << endl;
        return;
    }
};


int main(){
    Solution* obj = new Solution();
    ListNode* head = new ListNode(5);
    ListNode* second = new ListNode(10);
    ListNode* third = new ListNode(15);
    head->next = second;
    second->next = third;
    ListNode* cur = head;

    // Print Orignal Linked List
    obj->printLinkedList(head);

    ListNode *reversedList = obj->reverseList(head);

    
    // Print Reveresed Linked List
    obj->printLinkedList(reversedList);
    return 0;
}
