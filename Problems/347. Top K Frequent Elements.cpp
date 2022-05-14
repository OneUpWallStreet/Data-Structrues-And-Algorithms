#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;


class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            
            vector<int> answer;

            unordered_map<int,int> hashMap;

            for(int i=0;i<nums.size();i++){
                if(hashMap.find(nums[i]) == hashMap.end()){
                    hashMap[nums[i]] = 1;
                }
                else{
                    hashMap[nums[i]]++;
                }
            }


            for (auto& it: hashMap) {
                // answer.push_back(it.first)
                // if(it.second >= k){
                //     answer.push_back(it.first);
                // } 
            }



        return answer;
    }
};

void printVector(vector<int>& nums){
    cout << "-> ";
    for(int i=0;i<nums.size();i++){
        cout << " " << nums[i] << " " << endl;
    }
    cout << endl;
}

int main(){

    Solution solution;

    vector<int> input = {1,1,1,2,2,3};

    vector<int> answer = solution.topKFrequent(input,2);

    printVector(answer);

    

}