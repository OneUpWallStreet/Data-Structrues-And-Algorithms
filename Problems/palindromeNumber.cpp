#include<iostream>
#include<string>

using namespace std;


class Solution {
    public:
        bool isPalindrome(int x) {

            if(x<0){
                return false;
            }

            string s = to_string(x);
            

            int i = 0;
            int j = s.length()-1;

            while(i<j){
                if(s[i]==s[j]){
                    i++;
                    j--;
                }
                else{
                    return false;
                }
            }

            return true;

            
        }
};

int main(){
    int num = 11211;
    Solution solution;
    bool answer = solution.isPalindrome(num);
    cout << "Answer: " << answer << endl;
}