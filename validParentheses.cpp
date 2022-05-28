#include<iostream>
#include<vector>

using namespace std;

class Stack {


    public: 
        Stack(){
            
        }
        void push(char val){
            data.push_back(val);
        }

        void displayStack(){
            for(auto& it : data){
                cout << it << endl;
            }
        }

        bool isEmpty(){
            return data.empty();
        }

        

        char top(){
            return data.back();
        }

        char pop(){
            if(isEmpty()==false){
                char value = top();
                data.pop_back();
                return value;
            }
            return ' ';
        }

    private: 
        vector<char> data;

};

//  { ( [ {} ] ) }


class Solution {
        
    public:
        bool isValid(string s) {
            for(int i=0;i<s.length();i++){
                
                char parentheses = s[i];

                if(parentheses == '{' || parentheses == '(' || parentheses == '['){
                    stack.push(parentheses);
                    continue;
                }
                else if(parentheses == '}' || parentheses == ')' || parentheses == ']'){




                    char openBracket = stack.pop();

            

                    if(openBracket != getOpeningParenthesesForClosing(parentheses)){
                        return false;
                    }
                }
            }

            return stack.isEmpty();
        }



    private:
        Stack stack;

        char getOpeningParenthesesForClosing(char parentheses){
            if(parentheses == '}'){
                return '{';
            }
            else if(parentheses == ')'){
                return '(';
            }
            else{
                return '[';
            }
        }
};

int main(){
    Solution solution;
    string question = "()[]{}";
    bool answer = solution.isValid(question);
    cout << "The answer for parenthesis match is: " << answer << endl;
    return 0;
}


// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.

// Example 1:

// Input: s = "()"
// Output: true

// Example 2:

// Input: s = "()[]{}"
// Output: true

// Example 3:

// Input: s = "(]"
// Output: false

 

// Constraints:

//     1 <= s.length <= 104
//     s consists of parentheses only '()[]{}'.

