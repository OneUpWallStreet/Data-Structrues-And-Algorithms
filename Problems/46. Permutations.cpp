#include<iostream>

#include<vector>


using namespace std;

// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
// Example 2:

// Input: nums = [0,1]
// Output: [[0,1],[1,0]]
// Example 3:

// Input: nums = [1]
// Output: [[1]]
 

// Constraints:

// 1 <= nums.length <= 6
// -10 <= nums[i] <= 10
// All the integers of nums are unique.


class Solution {
    public:

        vector<vector<int>> permute(vector<int>& nums) {
            
            vector<vector<int>> result;

            if(nums.size()==1){
                return {nums};
            }

            for(int i=0;i<nums.size();i++){
                int element = nums[0];
                nums.erase(nums.begin());
                vector<vector<int>> perms = permute(nums);
                for(int j=0;j<perms.size();j++){
                    perms[j].push_back(element);
                    result.push_back(perms[j]);
                }
                nums.push_back(element);
                                
            }

            return result;
            
        }
};


int main(){

    Solution solution;

    vector<int> input = {1,2,3};

    vector<vector<int>> answer = solution.permute(input);

    
    
}