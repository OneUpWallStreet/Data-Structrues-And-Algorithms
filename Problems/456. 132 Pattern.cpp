#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>


using namespace std;

class Solution {
    public:

        bool nestedLoopSolution(vector<int> &nums){

            for(int i=0;i<nums.size();i++){
                for(int j=i+1;j<nums.size();j++){
                    for(int k=0;k<nums.size();k++){
                        if(nums[i] < nums[j] && nums[j] > nums[k] && nums[k] > nums[i]){
                            return true;
                        }
                    }
                }
            }
            return false;

        }


        bool didFindAppropriateValue(vector<int>& nums, int start, int end){

            cout << "i am called" << endl;

            // i < j < k

            // start = i 
            // end = j 
            if(hashMap[nums[start]]>hashMap[nums[end]]){
                cout << "start: " << nums[start] << " end: " << nums[end] << endl;
                cout << "hashmap[start]: "<< hashMap[nums[start]] << " hashmap[end]: " << hashMap[nums[end]] << endl;
                cout << "hashMap reject" << endl;
                return false;
            }

            int startValue = nums[start];
            int endValue = nums[end];

            for(int i=start;i<end;i++){

                // cout << i << endl;

                int currentValue = nums[i];

                // cout << "current Value: " << currentValue << endl;

                if(currentValue < endValue && currentValue > startValue && hashMap[currentValue] > hashMap[endValue] && hashMap[currentValue] > hashMap[startValue]){
                    return true;
                }
            }

            return false;

        }


        bool hashTableSolution(vector<int>& nums){

            if(nums.size()<3){
                return false;
            }

            int i,j;

            // Key Value Store -> For value in array store index
            // Key -> nums[i] & Value -> index
            for(i=0;i<nums.size();i++){
                // cout << "entering: " << nums[i] << " as: " << i << endl;
                hashMap[nums[i]] = i;
            }

            sort(nums.begin(),nums.end());
            
            // Print Sorted Vector
            for(int x =0;x<nums.size();x++){
                cout << " " << nums[x] << " ";
            }
            cout << endl;




            i = 0;  
            j = nums.size()-1;


            while(i<j){
                // cout << "i: " << i << endl;
                // cout << "j: " << j << endl;
                if(didFindAppropriateValue(nums,i,j)){
                    return true;
                }
                i++;
                j--;
            }

            return false;


        }
        

        bool find132pattern(vector<int>& nums) {

            for(int i=0;i<nums.size();i++){
                if(findPatternForIndex(nums,i)){
                    return true;
                }
            }
            return false;
        }

    private:

        unordered_map<int,int> hashMap;



        bool findPatternForIndex(vector<int>& nums,int index){

            if(index+1 > nums.size() || index+2 > nums.size()-1){
                return false;
            }

            cout << endl;
            cout << "nums[index] " <<  nums[index] << endl;
            cout << "nums[index+1] " << nums[index+1] << endl;
            cout << "nums[index+2] " << nums[index+2] << endl;
            cout << endl;

            if(nums[index] < nums[index+1] && nums[index+1] > nums[index+2] && nums[index+2] > nums[index]){

                cout << "index +2 value: " << index+2 << endl;
                cout << "is true" << endl;
                return true;
            }
            return false;
        }
};


int main(){

    Solution solution;

    vector<int> input = {3,5,0,7,4};

    for(int i=0;i<input.size();i++){
        cout << " " <<  input[i] << " ";
    }
    cout << endl;

    // bool answer = solution.find132pattern(input);
    // bool answer = solution.nestedLoopSolution(input);
    bool answer = solution.hashTableSolution(input);

    cout << "Answer is: " << answer << endl;

    // solution.find132pattern()
    
    
}

