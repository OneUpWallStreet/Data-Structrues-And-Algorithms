#include<vector>
#include<iostream>

using namespace std;

struct Node{
    int x;
    int y;
};


class Solution {
    public:
        int longestIncreasingPath(vector<vector<int>>& matrix) {
            int longestPath = 0;

            noOfRows = matrix.size();
            noOfColumns = matrix[0].size();

            initValueMatrix();

            for(int i=0;i<matrix.size();i++){
                for(int j=0;j<matrix[i].size();j++){
                    longestPath = max(longestPath,depthFirstSearch(matrix,{i,j}));
                }
            }

            return longestPath;
        }

    private:

        int depthFirstSearch(vector<vector<int>>& matrix,Node node){

            if(valueMatrix[node.x][node.y] != -1){
                return valueMatrix[node.x][node.y];
            }

            int pathValue = 1;
            
            vector<Node> validNodes = fetchValidNodes(matrix,node);

            for(int i=0;i<validNodes.size();i++){
                pathValue = max(pathValue,1 + depthFirstSearch(matrix,validNodes[i]));
            }

            valueMatrix[node.x][node.y] = pathValue;

            return pathValue;

        }

        vector<vector<int>> valueMatrix;
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


};

// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]


int main(){

    Solution solution;

    vector<vector<int>> input = {{9,9,4},{6,6,8},{2,1,1}};
    int answer = solution.longestIncreasingPath(input);
    cout << "Answer is: " << answer << endl;

    return 0;
}