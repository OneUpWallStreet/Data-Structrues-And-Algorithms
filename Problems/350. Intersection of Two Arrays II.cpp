#include<vector>
#include<unordered_map>
#include<iostream>

using namespace std;

class Solution {
    public:

        void createSet(vector<int> nums){
            for(int i=0;i<nums.size();i++){
                if(freqMap.find(nums[i]) == freqMap.end()){
                    freqMap[nums[i]] = 1;
                }
                else{
                    freqMap[nums[i]]++;
                }
            }
        }

        vector<int> createArray(vector<int> nums){
            vector<int> answer;

            for(int i=0;i<nums.size();i++){
                if(freqMap.find(nums[i]) != freqMap.end() && freqMap[nums[i]] > 0){
                    answer.push_back(nums[i]);
                    freqMap[nums[i]]--;
                }
            }

            return answer;

        }

        vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {

            vector<int> answer;

            if(nums1.size()>nums2.size()){
                createSet(nums1);
                return createArray(nums2);
            }
            else{
                createSet(nums2);
                return createArray(nums1);
            }

        }


    private: 
        unordered_map<int,int> freqMap;
};

void printVector(vector<int> nums){

    for(int i=0;i<nums.size();i++){
        cout << " " << nums[i] << " ";
    }
    cout << endl;
}

int main(){


// nums1 = [1,2,2,1]
// [2,2]

    vector<int> num1 = {4,9,5};
    vector<int> num2 = {9,4,9,8,4};

    // Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// 

    Solution solution;

    vector<int> answer =  solution.intersect(num1,num2);

    cout << "Size: " << answer.size() << endl;
    
    printVector(answer);

    return 0;
}