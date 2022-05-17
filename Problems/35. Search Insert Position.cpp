#include<vector>
#include<iostream>

using namespace std;


class Solution {
    public:

        int binarySearch(vector<int>& nums,int target, int left, int right){


            if(left<=right){

                int mid = left + (right - left)/2;


                if(nums[mid] == target){
                    return mid;
                }

                if(target<nums[mid]){
                    return binarySearch(nums,target,left,mid-1);
                }
                else{
                    return binarySearch(nums,target,mid+1,right);
                }



            }

        return left;

        }

        int searchInsert(vector<int>& nums, int target) {
            return binarySearch(nums,target,0,nums.size()-1);
        }
};

int main(){

    Solution solution;

    vector<int> nums = {1,3,5,6};

    int answer = solution.searchInsert(nums,7);

    cout << "Answer: " << answer << endl;

    return 0;
}