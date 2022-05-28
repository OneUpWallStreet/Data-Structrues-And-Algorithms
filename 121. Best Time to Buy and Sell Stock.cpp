#include<iostream>
#include<vector>


using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {

            int maxValue = 0;

            int i = 0;
            int j = i+1;

            while(j<prices.size()){
                
                if(prices[i]>prices[j]){
                    i++;
                    continue;
                }

                if(prices[i]<prices[j]){
                    maxValue = max(prices[j]-prices[i],maxValue);
                }

                j++;



            }

        
            

            return maxValue;

        }
};


// Input: prices = [7,1,5,3,6,4]
// Output 5

int main(){
    Solution solution;

    vector<int> input = {2,1,2,1,0,1,2};

    int answer = solution.maxProfit(input);

    cout << "Answer is: " << answer << endl;

}