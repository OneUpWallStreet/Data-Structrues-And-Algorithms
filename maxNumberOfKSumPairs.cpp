#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {   

        sort(nums.begin(),nums.end());

        if(nums.size()==0 || nums.size()==1){
            return 0;
        }

        int i = 0;
        int j = nums.size()-1;

        int operations = 0;

        while(i<j){

            if(nums[i]+nums[j]>k){
                j--;
                continue;
            }
            else if(nums[i]+nums[j]<k){
                i++;
                continue;
            }
            else if (nums[i]+nums[j]==k){
                operations++;
                i++;
                j--;
            }
        }

        return operations;

        
    }
};

int main(){
    Solution solution;
    vector<int> input = {3,1,3,4,3};
    int answer = solution.maxOperations(input,6);
    cout << "answer: " << answer << endl;
    return 0;
}