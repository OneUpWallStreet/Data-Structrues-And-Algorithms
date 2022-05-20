#include<vector>
#include<iostream>

using namespace std;


struct Node {
    int x;
    int y;
};


class Solution {
    private:

        vector<Node> fetchValidNodes(vector<vector<int>>& obstacleGrid, Node node){

            vector<Node> validPaths;

            // Go Down
            if(node.x + 1 < noOfRows && obstacleGrid[node.x+1][node.y] != 1){
                validPaths.push_back({node.x+1,node.y});
            }

            // Go Right
            if(node.y + 1 < noOfColumns && obstacleGrid[node.x][node.y+1] != 1){
                validPaths.push_back({node.x,node.y+1});
            }

            return validPaths;


        }

        void depthFirstSearch(vector<vector<int>>& obstacleGrid, Node node){

            // cout << "node.x: " << node.x << " " << "node.y: " << node.y << endl;

            if(node.x == noOfRows-1 && node.y == noOfColumns-1 && obstacleGrid[node.x][node.y] != 1){
                pathCount++;
                return;
            }

            vector<Node> validNodes = fetchValidNodes(obstacleGrid,node);

            // cout << "valid Nodes count: " << validNodes.size() << endl;

            for(int i=0;i<validNodes.size();i++){
                depthFirstSearch(obstacleGrid,validNodes[i]);
            }
            
        }
    public:
        int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
            
            noOfRows = obstacleGrid.size();
            noOfColumns = obstacleGrid[0].size();

            if(obstacleGrid[0][0] == 1){
                return pathCount;
            }

            depthFirstSearch(obstacleGrid,{0,0});

            return pathCount;

        }

    private: 
        int noOfColumns;
        int noOfRows;
        int pathCount = 0;
};

int main(){

    Solution solution;

    vector<vector<int>> grid = {{0,0,0},{0,1,0},{0,0,0}};

    int answer = solution.uniquePathsWithObstacles(grid);

    cout << "Answer is: " << answer << endl;

    return 0;
}