#include<vector>
#include<iostream>
using namespace std;


class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            
            int total = 1;
            int totalWithoutZero = 1;
            int zeroCounter = 0;

            vector<int> result;

            for(int i=0;i<nums.size();i++){
                total = total*nums[i];
                if(nums[i]==0){
                    zeroCounter++;
                }
                if(nums[i] != 0){
                    totalWithoutZero = totalWithoutZero*nums[i];
                }
            }            


            for(int i=0;i<nums.size();i++){

                if(nums[i] != 0){
                    result.push_back(total/nums[i]);
                }
                else if (zeroCounter > 1 && nums[i] == 0){
                    result.push_back(0);
                    // result.push_back(total/nums[i]);
                }
                else{
                    result.push_back(totalWithoutZero);

                }
            }


            return result;  
         }
};

void printVector(vector<int>& nums){
    cout << "-> ";
    for(int i=0;i<nums.size();i++){
        cout << " " << nums[i] << " ";
    }
    cout << endl;
}

int main(){
    Solution solution;

    vector<int> input = {0,0};

    vector<int> answer = solution.productExceptSelf(input);
    printVector(answer);

}
