#include<iostream>
#include<vector>

using namespace std;

// Implement strStr().

// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
 

// Constraints:

// 1 <= haystack.length, needle.length <= 104
// haystack and needle consist of only lowercase English characters.

class Solution {
    public:
        int strStr(string haystack, string needle) {

            if(needle.length()==0){
                return 0;
            }
            
            int windowStart = 0;
            int windowEnd = needle.length()-1;

            while(windowEnd<haystack.length()){
                if(containsSubString(windowStart,windowEnd,haystack,needle)){
                    return windowStart;
                }
                else{
                    windowStart++;
                    windowEnd++;
                }
            }
            return -1;

        }

    private:
        bool containsSubString(int start,int end, string haystack,string needle){
            for(int i=start, j=0;i<=end;i++,j++){
                if(haystack[i] != needle[j]){
                    return false;
                }
            }
            return true;
        }
};

int main(){
    string input = "hello";
    string needle = "ll";
    Solution solution;
    bool answer = solution.strStr(input,needle);
    cout << "Answer is: " << answer << endl;
}