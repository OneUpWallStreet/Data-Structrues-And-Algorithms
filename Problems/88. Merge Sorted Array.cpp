#include<vector>
#include<iostream>


using namespace std;

class Solution {
    public:
        void printVector(vector<int>& nums1){
            
            for(int i=0;i<nums1.size();i++){
                cout << " " << nums1[i] << " ";
            }

            cout << endl;

        }

        void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {


            for(int i = m, j = 0;i<nums1.size();i++,j++){
                nums1[i] = nums2[j];
            }

            sort(nums1.begin(),nums1.end());

        }
};

// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3


int main(){

    Solution solution;
    
    vector<int> n1 = {1,2,3,0,0,0};
    vector<int> n2 = {2,5,6};

    solution.merge(n1,3,n2,3);




    return 0;
}