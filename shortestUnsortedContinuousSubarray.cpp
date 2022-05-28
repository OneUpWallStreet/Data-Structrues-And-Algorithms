#include<iostream>
#include<vector>

using namespace std;

// Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

// Return the shortest such subarray and output its length.

// Example 1:

// Input: nums = [2,6,4,8,10,9,15]
// Output: 5
// Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

// Example 2:

// Input: nums = [1,2,3,4]
// Output: 0

// Example 3:

// Input: nums = [1]
// Output: 0

// Constraints:

//     1 <= nums.length <= 104
//     -105 <= nums[i] <= 105

 
// Follow up: Can you solve it in O(n) time complexity?

class Solution {
    public:

        int findUnsortedSubarray(vector<int>& nums) {

            if(nums.size()==0 || nums.size()==1){
                return 0;
            }

            vector<int> orignalVector = nums;

            sort(nums.begin(),nums.end());


            int firstIndex;
            bool foundFirst = false;
            bool foundLast = false;
            int lastIndex;
            int answer = 0;
            
            int i = 0;
            int j = nums.size()-1;

            while(i<=j){

                if(orignalVector[i]!=nums[i] && foundFirst != true){
                    firstIndex = i;
                    foundFirst = true;
                }
                if(orignalVector[j]!=nums[j] && foundLast != true){
                    lastIndex = j;
                    foundLast = true;
                }

                if(foundFirst==false){
                    i++;
                }
                
                if(foundLast==false){
                    j--;
                }

                if(foundFirst == true && foundLast == true){
                    break;
                }


            }


            if(foundFirst == true && foundLast == true){
                answer = (lastIndex+1) - firstIndex;
            }


            return answer;
            

        }
};

int main(){
    Solution solution;
    vector<int> input = {2,6,4,8,10,9,15};
    int answer = solution.findUnsortedSubarray(input);
    cout << "Answer is: " << answer << endl;
}