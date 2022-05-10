#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std;

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
//  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Example 2:

// Input: nums = []
// Output: []
// Example 3:

// Input: nums = [0]
// Output: []
 

// Constraints:

// 0 <= nums.length <= 3000
// -105 <= nums[i] <= 105

class Solution {
    public:


        void twoSum(vector<int>& nums,int index, int value){

            int i= index+1;
            int j = nums.size()-1;

            while(i<j){

                if(value+nums[i]+nums[j]==0){
                    
                    result.push_back({value,nums[i],nums[j]});

                    i++;

                    while(nums[i] == nums[i-1] && i < j){
                        i++;
                    }

                }
                else if(value+nums[i]+nums[j]<0){
                    i++;
                }
                else if(value+nums[i]+nums[j]>0){
                    j--;
                }
            }
            
        }
        

        vector<vector<int>> threeSum(vector<int>& nums) {

            sort(nums.begin(),nums.end());
                        

            for(int i=0;i<nums.size();i++){
                if(i>0 && nums[i] == nums[i-1]){
                    continue;
                }

                twoSum(nums,i,nums[i]);
            }

            return result;
        }

    private:
        vector<vector<int>> result;
};


int main(){

    Solution solution;
    vector<int> input =  {-1,0,1,2,-1,-4};

    vector<vector<int>> answer = solution.threeSum(input);

    cout << "Size: " << answer.size() << endl;
    return 0;
}