#include<iostream>
#include<vector>

using namespace std;

class Solution {
    public:
        void backTrack(int n_left,int index){

            if(n_left==0){
                counter++;
                return;
            }

            for(int i=index;i<vowels.size();i++){
                backTrack(n_left-1,i);
            }

        }

        int countVowelStrings(int n) {
            backTrack(n,0);
            return counter;
        }

    private:
        vector<char> vowels = {'a','e','i','o','u'};
        int counter = 0;
};

int main(){
    Solution solution;
    int answer = solution.countVowelStrings(33);
    cout << "Answer is: " << answer << endl;
}