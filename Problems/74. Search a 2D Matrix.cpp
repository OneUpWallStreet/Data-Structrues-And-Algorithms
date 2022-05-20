#include<vector>
#include<iostream>


using namespace std;

class Solution {
    public:

        bool binarySearch(vector<int> nums, int left,int right,int target){

            if(left<=right){

                int mid = left + (right - left)/2;


                if(nums[mid] == target){
                    return true;
                }

                if(target<nums[mid]){
                    return binarySearch(nums,left,mid-1,target);
                }
                else{
                    return binarySearch(nums,mid+1,right,target);
                }

            }

            return false;
        }

        bool searchMatrix(vector<vector<int>>& matrix, int target) {

            for(int i=0;i<matrix.size();i++){
                if(i+1==matrix.size()){
                    return binarySearch(matrix[i],0,matrix[i].size()-1,target);
                }
                else{
                    if(matrix[i][0] <= target && matrix[i+1][0] > target){
                        return binarySearch(matrix[i],0,matrix[i].size()-1,target);
                    }
                }
            }            

            return false;

        }
};

int main(){

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// 
    vector<vector<int>> input = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target = 3;
    Solution solution;
    bool answer = solution.searchMatrix(input,target);
    cout << "answer is:  " << answer << endl;
    return 0;
}   
