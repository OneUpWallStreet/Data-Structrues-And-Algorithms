#include<vector>
#include<iostream>

using namespace std;



class Solution {
    public:
        void moveZeroes(vector<int>& nums) {

            int i =0;
            int j =0;

            while(i<nums.size() && j<nums.size()){
                
                if(nums[i] == 0 && nums[j] == 0){
                    j++;
                    continue;
                }

                if(nums[i] == 0 &&  nums[j] != 0){
                    swap(nums[i],nums[j]);

                }

                i++;
                j++;

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

    // vector<int> input = {1};
    // vector<int> input = {1,2,3,4};
    vector<int> input = {0,2,3,4};


    
    cout << "initial: -> ";
    printVector(input);

    solution.moveZeroes(input);

    cout << "Final: ";
    printVector(input);




}