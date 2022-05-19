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

            for(int i=0;i<matrix.size();i++){
                for(int j=0;j<matrix[i].size();j++){
                    unordered_set< pair<int,int>,pair_hash> alreadyVisited;
                    depthFirstSearch(matrix,{i,j},{},alreadyVisited);
                    // breathFirstSearch(matrix,{i,j});
                }
            }

            return longestPath;
        }
    private:

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

        void breathFirstSearch(vector<vector<int>>& matrix, Node node){

            queue<pair<Node,vector<int>>> q;

            q.push({node,{}});

            while(q.size()>0){

                Node current = q.front().first;
                vector<int> path = q.front().second;

                q.pop();                
                
                vector<Node> validNodes = fetchValidNodes(matrix,current);

                path.push_back(matrix[current.x][current.y]);

                int currentPathSize = path.size();

                longestPath = max(longestPath,currentPathSize);


                for(int i=0;i<validNodes.size();i++){
                    q.push({validNodes[i],path});
                }


            }



        }

        void depthFirstSearch(vector<vector<int>>& matrix, Node node,vector<int> path,unordered_set< pair<int,int>,pair_hash> alreadyVisited){ 

            vector<Node> validNodes = fetchValidNodes(matrix,node);
            path.push_back(matrix[node.x][node.y]); 

            if(validNodes.size()==0){
                int currentPathLength = path.size();
                longestPath = max(longestPath,currentPathLength);
                return;
            }


            for(int i=0;i<validNodes.size();i++){
                    depthFirstSearch(matrix,validNodes[i],path,alreadyVisited);
            }
        }

        int longestPath = 0;
        int noOfRows;
        int noOfColumns;
    
};

// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]


int main(){

    Solution solution;
// [[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]]

    // vector<vector<int>> input = {{7,6,1,1}, {2,7,6,0}, {1,3,5,1}, {6,6,3,2}};
    vector<vector<int>> input = {{9,9,4},{6,6,8},{2,1,1}};

    int answer = solution.longestIncreasingPath(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}