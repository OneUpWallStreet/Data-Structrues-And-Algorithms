#include<iostream>
#include<unordered_set>
#include<unordered_map>

using namespace std;



// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
 

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

class Solution {
    public:
        bool isAnagram(string s, string t) {

            if(s.length() != t.length()){
                return false;
            }

            unordered_map<char,int> hashMap;


            for(int i=0;i<s.length();i++){
                
                if(hashMap.find(s[i]) == hashMap.end()){
                    hashMap[s[i]] = 1;
                }
                else{
                    hashMap[s[i]]++;
                }
            }

            for(int i=0;i<t.length();i++){

                if(hashMap.find(t[i]) == hashMap.end()){
                    return false;
                }
                else{
                    if(hashMap[t[i]] == 0){
                        return false;
                    }
                    else{
                        hashMap[t[i]]--;
                    }
                }
            }

            return true;
        }
};

