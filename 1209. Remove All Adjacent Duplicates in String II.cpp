#include<iostream>
#include<stack>
using namespace std;



// You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

// We repeatedly make k duplicate removals on s until we no longer can.

// Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

// Example 1:

// Input: s = "abcd", k = 2
// Output: "abcd"
// Explanation: There's nothing to delete.

// Example 2:

// Input: s = "deeedbbcccbdaa", k = 3
// Output: "aa"
// Explanation: 
// First delete "eee" and "ccc", get "ddbbbdaa"
// Then delete "bbb", get "dddaa"
// Finally delete "ddd", get "aa"

// Example 3:

// Input: s = "pbbcggttciiippooaais", k = 2
// Output: "ps"

 

// Constraints:

//     1 <= s.length <= 105
//     2 <= k <= 104
//     s only contains lower case English letters.



class Solution {
    public:
        string removeDuplicates(string s, int k) {

            if(s.length() == 0){
                return s;
            }

            for(int i=0;i<s.length();i++){
                
                if(stack.empty() == false && stack.top().first == s[i]){
                    stack.top().second++;
                    if(stack.top().second==k){
                        stack.pop();
                    }
                }
                else{
                    stack.push({s[i],1});
                }                
            }

            string answer;

            while(stack.empty()==false){
                while(stack.top().second != 0){
                    answer.push_back(stack.top().first);
                    stack.top().second -= 1;
                }
                stack.pop();
            }

            reverse(answer.begin(),answer.end());

            return answer;

        }
    private:
        stack<pair<char,int>> stack;
};


int main(){
    Solution solution;
    string input = "deeedbbcccbdaa";
    cout << input << endl;
    string answer = solution.removeDuplicates(input,3);
    cout << answer << endl;
    
}

