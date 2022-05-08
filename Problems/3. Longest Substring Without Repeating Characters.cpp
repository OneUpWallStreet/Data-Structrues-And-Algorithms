#include<iostream>
#include<unordered_map>
using namespace std;


class Solution {
    

    public:
        int lengthOfLongestSubstring(string s) {
            
            int highestCounter = 0;
            int i =0;

             for(int j=0;j<s.length();j++){
                
                // Not Found we should increase the window
                if( seen.find(s[j]) == seen.end()){
                    highestCounter = max(highestCounter,j-i+1);
                }
                else{
                    // check if we have seen the element in current window
                    if(seen[s[j]]<i){
                        highestCounter = max(highestCounter,j-i+1);
                    }
                    else{
                        i = seen[s[j]] + 1;
                    }
                }
                seen[s[j]] = j;
             }

             return highestCounter;
        }


    private:
        unordered_map<char,int> seen;
};




int main(){

    string input = "abba";

    cout << "string is: " << input << endl;

    Solution solution;
    int answer = solution.lengthOfLongestSubstring(input);
    
    cout << "Answer is: " << answer << endl;

}


            // int highest = 0;
            // int i = 0;

            // for(int j =0;j<s.length();j++){
            //     if(hashMap[s[j]]  == hashMap.end()){
            //         hashMap[s[j]] = 0;
            //     }
            //     else{
            //         hashMap[s[j]]++;
            //     }
            // }



            // if(s.length()==0){
            //     return 0;
            // }
            // else if(s.length()==1){
            //     return 1;
            // }

            // int i =0;
            // int j = s.length()-1;

            // int counter = 1;
            // int highestValue = 1;


            // while(i<j){
            //     if(s[i] != s[j]){
            //         i++;
            //     }
            //     else{
            //         j--;                    
            //     }
            // }

            // while(true){

            //     // cout << "i is:" << i << " & j is: " << j << endl;
                
            //     if(s[i] != s[j]){
            //         cout << "incrementing counter for: " << s[i] << " & "f << s[j] << endl;
            //         counter++;
            //         // cout << "counter is: " << counter << endl; 
            //         j++;
            //         i++;
            //         if(j==s.length()){
            //             break;
            //         }

            //     }
            //     else{
            //         if(counter>highestValue){
            //             highestValue = counter;
            //         }
            //         counter =0;
            //         i++;
            //     }
            // }

            // cout << "i: " << i << " j: " << j << endl;
  
            // return highestValue;

            
