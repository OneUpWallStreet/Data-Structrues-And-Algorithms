#include<iostream>
#include<unordered_map>

using namespace std;

// Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

 

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false

// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false

// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true

 

// Constraints:

//     1 <= ransomNote.length, magazine.length <= 105
//     ransomNote and magazine consist of lowercase English letters.


class Solution {
    public:
        bool canConstruct(string ransomNote, string magazine) {

            int i;
   
            for(i=0;i<magazine.length();i++){

                if(frequencyHashTable.find(magazine[i]) == frequencyHashTable.end()){
                    frequencyHashTable[magazine[i]] = 1;
                }
                else{
                    frequencyHashTable[magazine[i]] = frequencyHashTable[magazine[i]] + 1;
                }
            }

            for(i=0;i<ransomNote.length();i++){

                if(frequencyHashTable.find(ransomNote[i]) == frequencyHashTable.end()){
                    return false;
                }
                else{
                    if(frequencyHashTable[ransomNote[i]]<=0){
                        return false;
                    }
                    else{
                        frequencyHashTable[ransomNote[i]] = frequencyHashTable[ransomNote[i]]-1;
                        continue;
                    }  
                }

            }
    
            return true;
        }

    private:
        unordered_map<char,int> frequencyHashTable;
    
};


int main(){

    Solution solution;
    string s1 = "aa";
    string s2 = "ab";


    bool answer = solution.canConstruct(s1,s2);
    cout << "Answer: " << answer << endl;

}