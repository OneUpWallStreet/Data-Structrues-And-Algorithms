#include<iostream>
#include<vector>
#include<unordered_map>


using namespace std;



class Solution {
    public:

        void printPairVector(vector<pair<int,int>> input){
            cout << "-> ";
            for(int i=0;i<input.size();i++){
                cout << " { " << input[i].first << " , " << input[i].second << " } ";
            }
            cout << endl;
        }

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

            vector<pair<int,int>> freqVector;

            for (auto& it: hashMap) {
                freqVector.push_back({it.second,it.first});
            }

            make_heap(freqVector.begin(),freqVector.end());

            for(int i=0;i<k;i++){
                answer.push_back(freqVector.front().second);
                pop_heap(freqVector.begin(),freqVector.end());
                freqVector.pop_back();
            }

        return answer;
    }


};

void printVector(vector<int>& nums){
    cout << "-> ";
    for(int i=0;i<nums.size();i++){
        cout << " " << nums[i] << " ";
    }
    cout << endl;
}

int main(){

    Solution solution;

    vector<int> input = {1,1,1,2,2,3};

    vector<int> answer = solution.topKFrequent(input,2);

    printVector(answer);

    

}   