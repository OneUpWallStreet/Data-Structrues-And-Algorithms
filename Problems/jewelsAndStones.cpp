#include <iostream>

using namespace std;

// Input: jewels = "aA", stones = "aAAbbbb"
// Output: 3


class Solution {
    
    public:
        int numJewelsInStones(string jewels, string stones) {
            hashAndStoreJewels(jewels);
            return countJewelsInStones(stones);
        }


    private:
        int buckets[70] = {0};

        int countJewelsInStones(string stones){
            int count = 0;
            for(int i=0;i<stones.length();i++){
                int hashedValue = hashFunction(stones[i]);
                if(buckets[hashedValue]==1){
                    count++;
                }
            }
        return count;
        }

        void hashAndStoreJewels(string jewels){
            for(int i=0;i<jewels.length();i++){
                int hashedValue = hashFunction(jewels[i]);
                buckets[hashedValue] = 1;   
            }
            return;
        }


        int hashFunction(char key){

            int ia = (int)key;
            int hashedValue = ia % 70;
            return hashedValue;
        }

        
};

int main(){
    Solution solution;
    string jewels = "OEA";
    string stones = "xPYvv";
    int answer = solution.numJewelsInStones(jewels,stones);
    cout << "Number of Jewels in Stones: " << answer << endl;
    return 0;
}