#include<iostream>
#include<vector>
#include<unordered_map>
#include<set>
using namespace std;


class Solution {
    
    public:
    
        void dfs(vector<int> perms){


            if(perms.size()==permSize){
                result.push_back(perms);
                return;
            }

            for (const auto &myPair : hashMap ) {


                if(hashMap[myPair.first] > 0) {
                    perms.push_back(myPair.first);
                    hashMap[myPair.first] -= 1;

                    dfs(perms);

                    hashMap[myPair.first] += 1;
                    perms.pop_back();
                }


            }


        }


        vector<vector<int>> permuteUnique(vector<int>& nums) {

            permSize = nums.size();
            
            for(int i=0;i<nums.size();i++){
                if(hashMap.find(nums[i])==hashMap.end()){
                    hashMap[nums[i]] = 1;
                }
                else{
                    hashMap[nums[i]]++;
                }
            }

            dfs({});

            return result;

        }


    private:
        unordered_map<int,int> hashMap;
        int permSize;
        vector<vector<int>> result;


};

int main(){

    Solution solution;

    vector<int> input = {1,1,2};

    vector<vector<int>> answer = solution.permuteUnique(input);

    cout << "Size is: " << answer.size() << endl;

    for(int i=0;i<answer.size();i++){
        cout << " -> ";
        for(int j=0;j<answer[i].size();j++){
            cout << " " << answer[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}