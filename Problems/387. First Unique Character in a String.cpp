#include<vector>
#include<unordered_map>
#include<iostream>

using namespace std;

    class Solution {
        public:
            int firstUniqChar(string s) {
                
                int uniqueIndex;
                unordered_map<char,int> hashMap;
                
                for(int i=0;i<s.length();i++){
                    if(hashMap.find(s[i]) == hashMap.end()){
                        hashMap[s[i]] = 1;
                    }
                    else{
                        hashMap[s[i]]++;
                    }
                }

                for(int i=0;i<s.length();i++){
                    if(hashMap[s[i]] == 1){
                        return i;
                    }
                }

                return -1;
            }
    };
int main(){

    string s = "loveleetcode";

    Solution solution;
    
    int answer = solution.firstUniqChar(s);

    cout << "answer is: " << answer << endl;

}