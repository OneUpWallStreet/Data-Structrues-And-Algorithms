#include<vector>
#include<unordered_set>
#include<iostream>
#include<queue>

using namespace std;

struct Node{
    int x;
    int y;
};

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

class Solution {
    public:

        void printVector(vector<int> nums){
            for(int i=0;i<nums.size();i++){
                cout << " " << nums[i] << " ";
            }
            cout << endl;
        }

        int longestIncreasingPath(vector<vector<int>>& matrix) {
            
            noOfRows = matrix.size();
            noOfColumns = matrix[0].size();


            initValueMatrix();

            for(int i=0;i<matrix.size();i++){
                for(int j=0;j<matrix[i].size();j++){
                    if(valueMatrix[i][j] == -1){
                        depthFirstSearch(matrix,{i,j},{});
                    }
                }
            }


            for(int i=0;i<valueMatrix.size();i++){
                printVector(valueMatrix[i]);   
                for(int j=0;j<valueMatrix.size();j++){
                    longestPath = max(longestPath,valueMatrix[i][j]);
                }
            }

            return longestPath;
        }
    private:

        vector<vector<int>> valueMatrix;
        int longestPath = 0;
        int noOfRows;
        int noOfColumns;
    

        void initValueMatrix(){
            vector<vector<int>> matrix(noOfRows, vector<int>(noOfColumns));
                for(int i=0;i<noOfRows;i++){
                    for(int j=0;j<noOfColumns;j++){
                        matrix[i][j] = -1;
                    }
                }
            valueMatrix = matrix;
        }

        vector<Node> fetchValidNodes(vector<vector<int>>& matrix, Node node){
            
            vector<Node> validNodes;

            // Go Left
            if(node.y-1>=0 && matrix[node.x][node.y-1] > matrix[node.x][node.y]){
                validNodes.push_back({node.x,node.y-1});
            }

            // Go Right
            if(node.y+1<noOfColumns && matrix[node.x][node.y+1] > matrix[node.x][node.y]){
                validNodes.push_back({node.x,node.y+1});
            }

            // Go Bottom
            if(node.x-1 >= 0 && matrix[node.x-1][node.y] > matrix[node.x][node.y]){
                validNodes.push_back({node.x-1,node.y});
            }

            // Go Top
            if(node.x+1 < noOfRows && matrix[node.x+1][node.y] > matrix[node.x][node.y]){
                validNodes.push_back({node.x+1,node.y});
            }
            
            return validNodes;

        }

        void depthFirstSearch(vector<vector<int>>& matrix, Node node,vector<int> path){ 

            vector<Node> validNodes = fetchValidNodes(matrix,node);
            path.push_back(matrix[node.x][node.y]); 

            int currentPathLength = path.size();

            valueMatrix[node.x][node.y] = max(currentPathLength,valueMatrix[node.x][node.y]);

            for(int i=0;i<validNodes.size();i++){
                if(valueMatrix[validNodes[i].x][validNodes[i].y] == -1){
                    depthFirstSearch(matrix,validNodes[i],path);
                    // valueMatrix[node.x][node.y] = max(currentPathLength+valueMatrix[validNodes[i].x][validNodes[i].y],valueMatrix[node.x][node.y]);
                }
                else{
                    valueMatrix[node.x][node.y] = max(currentPathLength+valueMatrix[validNodes[i].x][validNodes[i].y],valueMatrix[node.x][node.y]);
                }
            }
        }


};

// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]


int main(){

    Solution solution;
// [[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]]

    vector<vector<int>> input = {{7,6,1,1}, {2,7,6,0}, {1,3,5,1}, {6,6,3,2}};
    // vector<vector<int>> input = {{9,9,4},{6,6,8},{2,1,1}};

    int answer = solution.longestIncreasingPath(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}