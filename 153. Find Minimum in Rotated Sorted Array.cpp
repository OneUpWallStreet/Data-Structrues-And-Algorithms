#include<vector>
#include<iostream>

using namespace std;


class Solution {

    
    public:

        int binarySearch(vector<int>& nums,int left,int right){

            if(left<=right){

                int mid = left + (right - left) /2;

                if(nums[mid] < nums[mid+1]){
                    return nums[mid+1];
                }

                if(nums[mid] < nums[mid+1]){
                    return nums[mid];
                }

                if(nums[mid] > nums[0]){
                    return binarySearch(nums,mid+1,right);
                }
                else{
                    return binarySearch(nums,left,mid-1);
                }

            }

        }

        int findMin(vector<int>& nums) {
            return binarySearch(nums,0,nums.size());
        }
};

int main() {

    return 0;
}