#include<iostream>

#include<vector>

using namespace std;


// int mid = firstIndex + (lastIndex-firstIndex)/2

class Solution {
    public:

        int binarySearch(vector<int>& nums, int target, int left,int right){
            
            if(right>=left){

                int mid = left + (right - left)/2;

                if(nums[mid]==target){
                    return mid;
                } 

                if(nums[mid]<target){
                    return binarySearch(nums,target,mid+1,nums.size()-1);
                }
                else{
                    return binarySearch(nums,target,left,mid-1);
                }

            }


            return -1;

        }

        int search(vector<int>& nums, int target) {
            return binarySearch(nums,target,0,nums.size()-1);
        }
};

int main(){

    Solution solution;
    vector<int> input = {-1,0,3,5,9,12};
    cout << "Answer is: " << solution.search(input,2) << endl;

    return 0;
}