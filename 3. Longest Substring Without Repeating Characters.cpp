#include<iostream>
#include<unordered_map>
using namespace std;


class Solution {
    public:
        int lengthOfLongestSubstring(string s) {

            int i =0;
            int j = 0;

            int maxLen = 0;

            unordered_set<int> mySet;

            while(j<s.length()){

                while(mySet.find(s[j]) != mySet.end()){
                    mySet.erase(mySet.find(s[i]));
                    i++;
                }

                mySet.insert(s[j]);
                maxLen = max(maxLen,j-i+1);

                j++;

            }

            return maxLen;

        }
};




int main(){

    string input = "abba";

    Solution solution;
    int answer = solution.lengthOfLongestSubstring(input);
    
    cout << "Answer is: " << answer << endl;

}


    