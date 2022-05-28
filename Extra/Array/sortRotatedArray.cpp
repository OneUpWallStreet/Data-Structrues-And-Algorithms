#include<iostream>
#include<vector>

using namespace std;


class Solution {
    public:
        void rotate(vector<int>& nums) {

            vector<int> answer;
            int sortIndex;

            for(int i=0;i<nums.size();i++){
                int value = nums[i];
                if(nums[i+1] < value){
                    sortIndex = i+1;
                    break;
                }
            }

            int incrementor = 0;

            while(incrementor<nums.size()){
                answer.push_back(nums[sortIndex]);
                if(sortIndex+1==nums.size()){
                    sortIndex=0;
                }
                else{
                    sortIndex++;
                }
                incrementor++;
            }

            nums = answer;
        }
};

void printVector(vector<int> input){
    cout << " [ ";

    for(int i=0;i<input.size();i++){
        cout << " " << input[i] << " ";
    }

    cout << " ] "<<endl;
}


int main(){


    vector<int> input = {4,5,6,7,0,1,2};
    Solution solution;
    printVector(input);    
    solution.rotate(input);
    printVector(input);
    return 0;
}