#include<vector>
#include<iostream>

using namespace std;



class Solution {
    public:
        int maxArea(vector<int>& height) {

            int i=0;
            int j = height.size()-1;

            int maxArea =0;

            while(i<j){
                maxArea = max(min(height[i],height[j])*(j-i),maxArea);
                if(height[i]<height[j]){
                    i++;
                }
                else{
                    j--;
                }                
            }


            return maxArea;
        }
};
int main(){

    Solution solution;

    // vector<int> input = {1,8,6,2,5,4,8,3,7};
    vector<int> input = {1,1};

    int answer = solution.maxArea(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}