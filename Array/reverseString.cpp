#include<iostream>
#include<vector>

using namespace std;

class Solution {
    public:
        void reverseString(vector<char>& s) {

            int i=0;
            int j = s.size() - 1;

            while(i<j){
                swapVectorElements(s,i,j);
                i++;
                j--;
            }
        }


        void printVector(vector<char> s){
            for(auto& it : s){      
                cout << " " << it << " ";
            }
            cout << endl;
        }

    private:
        void swapVectorElements(vector<char>& s, int i,int j){
            int temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }

};





int main(){

    Solution solution;

    vector<char> input;
    input.push_back('h');
    input.push_back('e');
    input.push_back('l');
    input.push_back('l');
    input.push_back('o');


    solution.printVector(input);
    solution.reverseString(input);
    // solution.secondString(input);
    solution.printVector(input);
    

    // cout << input << endl;

}