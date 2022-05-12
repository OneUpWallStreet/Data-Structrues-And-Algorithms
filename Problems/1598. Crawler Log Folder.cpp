#include<vector>
#include<stack>
#include<iostream>



using namespace std;

// "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
// "./" : Remain in the same folder.
// "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

class Solution {
public:

    bool isRemainInSameFolder(string log){
        if(log[0]=='.' && log[1] == '/'){
            return true;
        }
        return false;
    }

    bool isMoveToParentOfCurrent(string log){
        if(log[0] == '.' && log[1] == '.' && log[2] == '/'){
            return true;
        }
        return false;
    }

    bool isMoveToChildDirectory(string log){
        if(isRemainInSameFolder(log) == false && isMoveToParentOfCurrent(log) == false){
            return true;
        }
        return false;
    }

    int minOperations(vector<string>& logs) {

        int counter = 0;

        for(int i=0;i<logs.size();i++){
            string log = logs[i];
            if(isMoveToChildDirectory(log)){
                counter++;
            }
            else if (isMoveToParentOfCurrent(log)){
                counter = max(counter-1,0);
            }
        }

        return counter;

    }
};

int main(){

    Solution solution;

    // vector<string> input = {"d1/","d2/","./","d3/","../","d31/"};
    vector<string> input = {"d1/","../","../","../"};
    int answer = solution.minOperations(input);

    cout << "Answer is:  " << answer << endl;


}