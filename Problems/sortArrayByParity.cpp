#include<iostream>
#include<vector>

using namespace std;


// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

// Return any array that satisfies this condition.

// Example 1:

// Input: nums = [3,1,2,4]
// Output: [2,4,3,1]
// Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

// Example 2:

// Input: nums = [0]
// Output: [0]


// Constraints:

//     1 <= nums.length <= 5000
//     0 <= nums[i] <= 5000


class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        if(nums.size()==0 || nums.size()==1){
            return nums;
        }
        int i=0;
        int j = nums.size()-1;
        while(i<j){
            if(nums[i]%2==0){
                i++;
                continue;
            }
            if(nums[j]%2==0){
                swap(nums[i],nums[j]);
            }
            j--;
        }

        return nums;
    }

    void printVector(vector<int>& nums){
        for(auto& it: nums){
            cout << " " << it << " ";
        }
        cout << endl;
    }
};


int main(){
    Solution solution;
    vector<int> input = {1,0,3};
    solution.printVector(input);
    vector<int> answer = solution.sortArrayByParity(input);
    solution.printVector(answer);
    return 0;
}