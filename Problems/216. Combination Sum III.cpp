#include<iostream>
#include<vector>
#include<unordered_set>
#include<set>
using namespace std;


// Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

// Only numbers 1 through 9 are used.
// Each number is used at most once.
// Return a list of all possible valid combinations. The list must not contain the same combination twice,
//  and the combinations may be returned in any order.

 

// Example 1:

// Input: k = 3, n = 7
// Output: [[1,2,4]]
// Explanation:
// 1 + 2 + 4 = 7
// There are no other valid combinations.
// Example 2:

// Input: k = 3, n = 9
// Output: [[1,2,6],[1,3,5],[2,3,4]]
// Explanation:
// 1 + 2 + 6 = 9
// 1 + 3 + 5 = 9
// 2 + 3 + 4 = 9
// There are no other valid combinations.
// Example 3:

// Input: k = 4, n = 1
// Output: []
// Explanation: There are no valid combinations.
// Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and 
// since 10 > 1, there are no valid combination.
 

// Constraints:

// 2 <= k <= 9
// 1 <= n <= 60


// Bottle Necks
// It sorts each array to make them unique
// It loops through to calculate sum
// It calculates impossible values
// When you store sum also check if its greater than target to prune it

class Solution {


    public:


        void backTrackImproved(vector<int> nums, int k, int start,int sum){

            if(k==0){
                if(sum==target){
                    result.push_back(nums);
                }
                return;
            }

            for(int i=start;i<10 && i<target;i++){
                 nums.push_back(i);
                 backTrackImproved(nums,k-1,i+1,sum+i);
                 nums.pop_back();
            }

        }

        vector<vector<int>> combinationSum3(int k, int n) {
            target = n;
            vector<int> nums;
            backTrackImproved(nums,k,1,0);
            return result;
        }

    private:
        vector<vector<int>> result;
        int target;
};




int main(){

    Solution solution;
    vector<vector<int>> answer = solution.combinationSum3(9,45);

    cout << "Size is: " << answer.size() << endl;

    for(int i=0;i<answer.size();i++){

        cout << " " << i << " ->";
        
        for(int j=0;j<answer[i].size();j++){
            cout << " " << answer[i][j] << " ";
        }

        cout << endl;

    }


    return 0;
}

        // Orignal Submission
        // void dfsBackTracking(vector<int> nums,int number,int kLeft,int sum){

        //     if(result.size()==1){
        //         if(result[0].size()==9){
        //             return;
        //         }
        //     }

        //     // cout << "Backtracking for: " << endl;
        //     if(kLeft==0){
        //         sort(nums.begin(),nums.end());              
        //         if(resultSet.find(nums) != resultSet.end()){
        //             return;
        //         }
        //         if(target==sum){
        //             resultSet.insert(nums);
        //             result.push_back(nums);
        //         }
        //         return;
        //     }

        //     alreadyUsed.insert(number);

        //     for(int i=1;i<10;i++){
        //         if(alreadyUsed.find(i) == alreadyUsed.end()){
        //             if(sum+i>target){
        //                 continue;
        //             }
        //             vector<int> newNums = nums;
        //             newNums.push_back(i);
        //             dfsBackTracking(newNums,i,kLeft-1,sum+i);
        //         }
        //     }

        //     alreadyUsed.erase(alreadyUsed.find(number));

        //     return;
        
        // }
