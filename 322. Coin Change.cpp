#include<vector>
#include<iostream>

using namespace std;


class Solution {

    private:

        void depthFirstTraversal(vector<int>& coins,int target,int pathLenght){
      
            pathLenght++;

            if(target<0){
                return;
            }
            else if(target == 0){
                minCoins = min(pathLenght,minCoins);
                return;
            }

            for(int i=0;coins.size();i++){
                if(target-coins[i]>= 0){
                    depthFirstTraversal(coins,target-coins[i],pathLenght);
                }
            }

            
        }

    public:

        int coinChange(vector<int>& coins, int amount) {

            for(int i=0;i<coins.size();i++){
                cout << "ho" << endl;
                depthFirstTraversal(coins,amount-coins[i],0);
            }

            return minCoins;   
        }

    private: 
        int minCoins;
        
};

int main(){

    vector<int> coins = {1,2,5};
    int amount = 7;

    Solution solution;
    
    int answer = solution.coinChange(coins,amount);

    cout << "Answer is: " << answer << endl;


    return 0;
}