#include<vector>
#include<iostream>

using namespace std;



class Solution {
    public:
        int maxArea(vector<int>& height) {

            int i=0;
            int j = height.size()-1;

            int maxArea =0;
            int b;

            for(int i=0;i<height.size();i++){
                for(int j=i+1;j<height.size();j++){
                    int h = min(height[i],height[j]);
                    b = j-i;
                    maxArea = max(maxArea,h*breath);
                    
                }
            }
            
            return maxArea;
        }
};

int main(){

    Solution solution;

    vector<int> input = {1,8,6,2,5,4,8,3,7};

    int answer = solution.maxArea(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}