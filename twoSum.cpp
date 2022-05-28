#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>


using namespace std;


class Solution {

    private: 
        unordered_map<int,int> hashMap;

    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> answer;
            for(int i=0;i<nums.size();i++){
                int toFind = target - nums[i];
                if(hashMap.find(toFind) != hashMap.end()){
                    answer.push_back(i);
                    answer.push_back(hashMap[toFind]);
                    return answer;
                }

                hashMap[nums[i]] = i;
            }
            return answer;
        }


};

int main(){

    Solution solution;

    vector<int> input = {3,2,4};

    vector<int> answer = solution.twoSum(input,6);

    for(auto& it: answer){
        cout << " " <<  it << " ";
    }



    return 0;
}