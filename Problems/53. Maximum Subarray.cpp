#include<vector>
#include<iostream>

using namespace std;


class Solution {
    public:
        int maxSubArray(vector<int>& nums) {

            int sum = 0;

            for(int i=0;i<nums.size();i++){
                for(int j=i;j<nums.size();j++){
                    int currentSum = 0;
                    for(int k=i; k<j;k++){
                        currentSum += nums[k];
                    }
                    sum = max(sum,currentSum);
                }

            }
            

            return sum;
        }
};

             
int main(){
    Solution solution;

    vector<int> input = {-2,1,-3,4,-1,2,1,-5,4};

    int answer = solution.maxSubArray(input);

    cout << "Answer: " << answer << endl;

}
