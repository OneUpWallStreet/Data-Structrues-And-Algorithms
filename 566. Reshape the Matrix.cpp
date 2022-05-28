#include<vector>
#include<iostream>

using namespace std;


class Solution {
    public:

        vector<int> matrixToArray(vector<vector<int>>& mat){

            vector<int> arr;

            for(int i=0;i<mat.size();i++){
                for(int j=0;j<mat[i].size();j++){
                    arr.push_back(mat[i][j]);
                }
            }

            return arr;
        }

        vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {


            vector<vector<int>> answerMatrix;

            if(mat.size()*mat[0].size() != r*c){
                return mat;
            }

            vector<int> flatMatrix = matrixToArray(mat);

            // if(flatMatrix.size() != r*c){
                // return mat;
            // }

            int index = 0;

            for(int i=0;i<r;i++){
                vector<int> colMatrix;
                for(int j=0;j<c;j++){
                    colMatrix.push_back(flatMatrix[index]);
                    index++;
                }
                answerMatrix.push_back(colMatrix);
            }


            return answerMatrix;
            
        }
};

// Input: mat = [[1,2],[3,4]], r = 1, c = 4


void printVector(vector<int> nums){

    for(int i=0;i<nums.size();i++){
        cout << " " << nums[i] << " ";
    }
    cout << endl;
}

void printMatrix(vector<vector<int>> mat){
    for(int i=0;i<mat.size();i++){
        printVector(mat[i]);
    }

}

int main(){

    Solution solution;

// [[1,2],[3,4]]
// 2
// 4

    vector<vector<int>> input = {{1,2}};

    vector<vector<int>> sol = solution.matrixReshape(input,1,1);

    cout << "Sol Size: " << sol.size() << endl;

    printMatrix(sol);
}
