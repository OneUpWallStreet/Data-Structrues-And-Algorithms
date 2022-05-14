#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

// Input: nums = [100,4,200,1,3,2]
// Output: 4

class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {

            int counter = 1;
            int longest = 1;

            unordered_set<int> used;

            sort(nums.begin(),nums.end());


            for(int i=0;i<nums.size();i++){
                cout << "inserting: "<< nums[i] << endl;
                mySet.insert(nums[i]);
            }

            for(int i=0;i<nums.size();i++){
                
                if(used.find(nums[i]) != used.end()){
                    continue;
                }

                if(mySet.find(nums[i]+1) != mySet.end()){
                    used.insert(nums[i]);
                    counter++;
                }
                else{
                    longest = max(counter,longest);
                    counter = 1;
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