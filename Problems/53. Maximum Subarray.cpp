#include<vector>
#include<iostream>

using namespace std;


class Solution {
    public:
        int maxSubArray(vector<int>& nums) {

            int maxSum = nums[0];
            int currentSum = 0;


            for(int i=0;i<nums.size();i++){

                if(currentSum<0){
                    currentSum = 0;
                }

                currentSum += nums[i];

                maxSum = max(maxSum,currentSum);

            }

            return maxSum;
        }
};

             
int main(){
    Solution solution;

    vector<int> input = {-2,1,-3,4,-1,2,1,-5,4};

    int answer = solution.maxSubArray(input);

    cout << "Answer: " << answer << endl;

}
