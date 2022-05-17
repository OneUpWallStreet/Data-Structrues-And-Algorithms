#include<vector>
#include<iostream>

using namespace std;



class Solution {
    public:
        void moveZeroes(vector<int>& nums) {


            int i;
            int j = nums.size()-1;

            for(int k = nums.size()-1;k>=0;k--){
                if(nums[k] == 0){
                    i = k;
                    break;
                }
            }


            while(i >= 0 && j >= 0){

                if(nums[j] == 0){
                    j--;
                    continue;
                } 

                swap(nums[i],nums[j]);

                if(nums[i] == 0){
                    j--;
                }
    
                i--;

            }

            
            
        }
};

void printVector(vector<int>& nums1){
    
    for(int i=0;i<nums1.size();i++){
        cout << " " << nums1[i] << " ";
    }

    cout << endl;

}
int main(){

    Solution solution;

    // vector<int> input = {0,1,0,3,12};
    vector<int> input = {0,2,3,4};


    
    cout << "initial: -> ";
    printVector(input);

    solution.moveZeroes(input);

    cout << "Final: ";
    printVector(input);




}