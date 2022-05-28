#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

// Input: nums = [100,4,200,1,3,2]
// Output: 4

class Solution {
    public:

        int countSequence(vector<int>& nums,int num){
            int counter = 1;
            while(true){
                if(mySet.find(num+1) != mySet.end()){
                    num++;
                    counter++;
                }
                else{
                    return counter;
                }
            }
        }

        int longestConsecutive(vector<int>& nums) {

            if(nums.size()==0){
                return 0;
            }

            int longest = 1;

            for(int i=0;i<nums.size();i++){
                mySet.insert(nums[i]);
            }

            unordered_set<int> sequenceSet;

            for(int i=0;i<nums.size();i++){
                if(mySet.find(nums[i]-1) == mySet.end() && sequenceSet.find(nums[i]-1) == sequenceSet.end()){
                    sequenceSet.insert(nums[i]-1);
                    longest = max(countSequence(nums,nums[i]),longest);
                }
            }
            
            return longest;
        }

    private:
        unordered_set<int> mySet;
};

int main(){
    Solution solution;

    vector<int> input = {0,3,7,2,5,8,4,6,0,1};
    // vector<int> input = {100,4,200,1,3,2};

    int answer = solution.longestConsecutive(input);

    cout << "Answer: " << answer << endl;

    cout << "Hello World" << endl;
}