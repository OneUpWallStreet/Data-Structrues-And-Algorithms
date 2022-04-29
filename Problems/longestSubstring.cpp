#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstring(string s) {

            int counter = 0;
            int highestCounter = 0;
            vector<int> storedHashes;
            
            for(int i=0;i<s.length();i++){
                
                int hashedValue = hashFunction(s[i]);

                cout << "Char is "<< s[i] << " Hash Value is " << hashedValue << endl;
 
                // Alphabet is already encountered, clear bucket 
                if(buckets[hashedValue]==1){
                    if(counter > highestCounter){
                        highestCounter = counter;
                    }
                
                    for(auto& it : storedHashes){
                        // cout << "It: " << it << endl;
                        buckets[it] = 0;
                    }

                    storedHashes.clear();
                    counter = 0;
                        
                }
                buckets[hashedValue] = 1;
                storedHashes.push_back(hashedValue);
                counter++;
            }

            if(counter>highestCounter){
                highestCounter=counter;
            }

            return highestCounter;
        }

    private:
        int buckets[50000] = {0};

        int hashFunction(char key){
            int intKey = (int)key;
            int hashedValue = intKey % 129;
            return hashedValue;
        }
        


};

// Does not work, solution is wrong.
int main(){
    Solution solution;
    string s = "pwdda";
    int answer = solution.lengthOfLongestSubstring(s);
    cout << "Longest Substring size is: "<< answer << endl;
    return 0;
}