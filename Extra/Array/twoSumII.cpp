#include<iostream>
#include<vector>

using namespace std;


// Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

// Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

// The tests are generated such that there is exactly one solution. You may not use the same element twice.

// Your solution must use only constant extra space.

 

// Example 1:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

// Example 2:

// Input: numbers = [2,3,4], target = 6
// Output: [1,3]
// Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

// Example 3:

// Input: numbers = [-1,0], target = -1
// Output: [1,2]
// Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

//  1 3 6 7 9 20 Target -> 15

// Constraints:

//     2 <= numbers.length <= 3 * 104
//     -1000 <= numbers[i] <= 1000
//     numbers is sorted in non-decreasing order.
//     -1000 <= target <= 1000
//     The tests are generated such that there is exactly one solution.



class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size()-1;
        vector<int> answer;
        int sum;
        while(i<j){
            sum = numbers[i]+numbers[j];
            if(sum==target){
                answer.push_back(i+1);
                answer.push_back(j+1);
                break;
            }
            else if(sum>target){
                j--;
            }
            else if(sum<target){
                i++;
            }
        }
        return answer;
    }

    void printVector(vector<int>& vec){
        cout << "[ ";
        for(auto& it: vec){
            cout << " " << it << " ";
        }
        cout << " ]" << endl;
    }
};

int main(){

    // Solution solution;
    Solution solution;
    vector<int> input = {-1,0};
    vector<int> answer = solution.twoSum(input,-1);    
    solution.printVector(answer);    


}

