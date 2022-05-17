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

            int i = m-1;
            int j = n-1;

            int lastIndex = m+n-1;

            while(i>=0 && j>=0){
                
                if(nums2[j]>=nums1[i]){
                    nums1[lastIndex] = nums2[j];
                    j--;
                    lastIndex--;
                }
                else {
                    nums1[lastIndex] = nums1[i];
                    i--;
                    lastIndex--;
                }

            }

            while(j>=0){
                nums1[lastIndex] = nums2[j];
                lastIndex--;
                j--;
            }

        }
};

// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3


int main(){

    Solution solution;
    
    // vector<int> n1 = {1,2,3,0,0,0};
    // vector<int> n2 = {2,5,6};

    vector<int> n1 = {0};
    vector<int> n2 = {1};


//     [0]
// 0
// [1]
// 1




    solution.merge(n1,0,n2,1);

    solution.printVector(n1);




    return 0;
}

            // for(int i = m, j = 0;i<nums1.size();i++,j++){
            //     nums1[i] = nums2[j];
            // }

            
            
            // sort(nums1.begin(),nums1.end());