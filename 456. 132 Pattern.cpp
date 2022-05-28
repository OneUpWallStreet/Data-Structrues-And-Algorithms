#include<iostream>
#include<vector>
#include<stack>


using namespace std;



class Solution {
    public:
        bool find132pattern(vector<int>& nums) {
            
            stack<int> stack;
            
            for(int i=0;i<nums.size();i++){
                
            }
            

        }
};

int main(){

    Solution solution;

    vector<int> input = {3,5,0,7,4};

    for(int i=0;i<input.size();i++){
        cout << " " <<  input[i] << " ";
    }
    cout << endl;

    bool answer = solution.find132pattern(input);
    // bool answer = solution.nestedLoopSolution(input);
    // bool answer = solution.hashTableSolution(input);

    cout << "Answer is: " << answer << endl;

    // solution.find132pattern()
    
    
}

