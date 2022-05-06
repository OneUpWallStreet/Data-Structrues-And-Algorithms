#include<iostream>
#include<unordered_map>

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
            

            if(doesContainDuplicates(s,k)==false){
                return s;
            }

            return removeDuplicates(removeFirstDuplicateElements(s,k),k);

        }

        

        string removeFirstDuplicateElements(string s,int k){

            string newString;
            bool foundFirstDupl = false;

            for(int i=0;i<s.length();i++){
                if(isDuplicateWithFreq(s,k,i)==true && foundFirstDupl == false){
                    i += k-1;
                    foundFirstDupl = true;
                    continue;
                }
                newString.push_back(s[i]);
            }

            return newString;
        }

        bool doesContainDuplicates(string s,int k){
            for(int i=0;i<s.length();i++){
                if(isDuplicateWithFreq(s,k,i) == true){
                    return true;
                }
            }

            return false;
        }

        bool isDuplicateWithFreq(string s,int k,int index){
            char charAtIndex = s[index];
            for(int i=index;i<index+k;i++){
                if(s[i] == charAtIndex){
                    continue;
                }
                else{
                    return false;
                }
            }
            return true;
        }

        
};


int main(){
    Solution solution;
    string input = ;
    cout << input << endl;
    string answer = solution.removeDuplicates(input,3);
    cout << answer << endl;
    
}



            // for(int i=0;i<s.length();i++){
                // if(isDuplicateWithFreq(s,k,i)){
                    // s = removeKElements(s,k,i);
                // }
            // }



            // for(int i =0;i<s.length();i++){
                // if(isDuplicateWithFreq(s,k,i)==true){}
            // }

            // for(int i=0;i<s.length();i++){
            //     if(isDuplicateWithFreq(s,k,i)){
            //         i += k-1;
            //         removeDuplicates(s,k);

            //     }
            // }

            // return s;

            
            // string answer;

            // for(int i=0;i<s.length();i++){
            //     if(isDuplicateWithFreq(s,k,i)){
            //         i += k-1; 
            //         continue;
            //     }
            //     else{
            //         answer.push_back(s[i]);
            //     }
            // }

            // return answer;


        //             string removeFirstDuplicateElements(string s,int k){

        //     string newString;
        //     bool foundFirstDupl = false;

        //     for(int i=0;i<s.length();i++){

        //         if(isDuplicateWithFreq(s,k,i)==true && foundFirstDupl == false){
        //             i += k-1;
        //             foundFirstDupl = true;
        //             continue;
        //         }
                
        //         newString.push_back(s[i]);

        //         // if(i==index){
        //         //     i += k-1;
        //         // }
        //         // else{
        //         //     newString.push_back(s[i]);
        //         // }
        //     }

        //     return newString;
        // }