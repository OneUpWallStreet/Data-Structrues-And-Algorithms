#include<iostream>
#include<vector>

using namespace std;
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]

// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

 

// Constraints:

//     The number of nodes in each linked list is in the range [1, 100].
//     0 <= Node.val <= 9
//     It is guaranteed that the list represents a number that does not have leading zeros.


 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

            int num1,num2;

            ListNode* answer = new ListNode();

            l1 = reverseLinkedList(l1);
            l2 = reverseLinkedList(l2);

            num1 = convertLinkedListToInt(l1);
            num2 = convertLinkedListToInt(l2);

            int sum = num1+num2;

            answer = convertIntegerToToLinkedList(sum);

            return answer;
        }


        void printLinkedList(ListNode* head){
            ListNode* cur = head;
            while(true){
                cout << cur->val << endl;
                if(cur->next == nullptr){
                    break;
                }
                cur = cur->next;                
            }
        }

        void addElementToLinkedList(ListNode* head,int value,int size){

            ListNode* cur = head;
            
            if(size==0){
                head->val = value;
                return;
            }

            while(cur->next != nullptr){
                cur = cur->next;
            }
            ListNode* newNode = new ListNode(value);
            cur->next = newNode;
            return;
        }

    

    private:

        ListNode* convertIntegerToToLinkedList(int number){
            
            ListNode* cur = new ListNode();
            int size = 0;

            while(number!=0){
                addElementToLinkedList(cur,number%10,size);
                size++;
                number /= 10;
            }

            return cur;
        }

        int convertLinkedListToInt(ListNode* head){

            ListNode* cur = head;
            vector<int> numArray;
            while(true){
                numArray.push_back(cur->val);
                if(cur->next == nullptr){
                    break;
                }
                cur = cur->next;
            }
            int number = 0;
            for(auto& it: numArray){
                number = number*10 + it;
            }

            return number;


        }

        ListNode* reverseLinkedList(ListNode* head){
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

};


int main(){

    Solution solution;

    ListNode* head1 = new ListNode(); 
    ListNode* head2 = new ListNode();

    solution.addElementToLinkedList(head1,2,0);
    solution.addElementToLinkedList(head1,4,1);
    solution.addElementToLinkedList(head1,3,2);


    solution.addElementToLinkedList(head2,5,0);
    solution.addElementToLinkedList(head2,6,1);
    solution.addElementToLinkedList(head2,4,2);

    ListNode* answer = solution.addTwoNumbers(head1,head2);

    solution.printLinkedList(answer);
    return 0;
}

