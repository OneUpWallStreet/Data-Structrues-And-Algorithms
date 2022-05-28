#include<vector>
#include<iostream>

using namespace std;


class Solution {
    public:

        void backTrack(vector<int>& nums,int index, vector<int> subset){

            if(index == nums.size()){
                result.push_back(subset);
                return;
            }

            // Choose to add value to subset

            subset.push_back(nums[index]);
            backTrack(nums,index+1,subset);

            // Choose to not add value to subset
            subset.pop_back();
            backTrack(nums,index+1,subset);
                
        }

        vector<vector<int>> subsets(vector<int>& nums) {
            backTrack(nums,0,{});
            return result;
        }


    private:
        vector<vector<int>> result;
};

int main(){
    Solution solution;
    vector<int> input = {1,2,3};
    vector<vector<int>> answer = solution.subsets(input);
}
