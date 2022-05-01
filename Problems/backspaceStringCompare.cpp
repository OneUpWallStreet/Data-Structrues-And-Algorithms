#include<iostream>
#include<vector>

using namespace std;

// Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

// Note that after backspacing an empty text, the text will continue empty.

 

// Example 1:

// Input: s = "ab#c", t = "ad#c"
// Output: true
// Explanation: Both s and t become "ac".

// Example 2:

// Input: s = "ab##", t = "c#d#"
// Output: true
// Explanation: Both s and t become "".

// Example 3:

// Input: s = "a#c", t = "b"
// Output: false
// Explanation: s becomes "c" while t becomes "b".

 

// Constraints:

//     1 <= s.length, t.length <= 200
//     s and t only contain lowercase letters and '#' characters.

// Follow up: Can you solve it in O(n) time and O(1) space?

class Stack {

    public:
        vector<char> data;

        void push(char value){
            data.push_back(value);
        }

        bool pop(){
            if(data.empty()){
                return false;
            }
        
            data.pop_back();
            return true;
        }

        void printVector(){
            for(auto& it: data){
                cout << it << endl;
            }
        }
};

class Solution {
    public:
        bool backspaceCompare(string s, string t) {

            int i;

            Stack sStack;
            Stack tStack;

            for(i=0;i<s.length();i++){
                char c = s[i];
                if(c=='#'){
                    sStack.pop();
                }
                else{
                    sStack.push(c);
                }
            }


            for(i=0;i<t.length();i++){
                char c = t[i];
                if(c=='#'){
                    tStack.pop();
                }
                else{
                    tStack.push(c);
                }
            }


            if(sStack.data == tStack.data){
                return true;
            }
            return false;
        }
};
 

int main(){
    Solution solution;
    string s1 = "ab##";
    string s2 = "c#d#";
    bool answer = solution.backspaceCompare(s1,s2);
    cout << "Answer: " << answer << endl;
}