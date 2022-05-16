#include<vector>
#include<stack>
#include<unordered_set>
#include<stack>
#include<queue>
#include<iostream>

using namespace std;

struct pair_hash {
    inline size_t operator()(const pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

class Solution {
    public:

        void breathFirstSearch(){

            pair<int,int> node = {0,0};
            alreadyVisited.insert(node);


            queue<pair<pair<int,int>,int>> q;

            q.push({node,1});

            while(q.size()>0){

                int x = q.front().first.first;
                int y = q.front().first.second;

                cout << " At Node: { " << x << " , " << y << " }" << endl;

                int distance = q.front().second;

                if( q.front().first == finalNode){
                    pathLength = distance;
                    break;
                }
                

                q.pop();

                vector<pair<int,int>> validPaths = getValidPathsForNode({x,y}); 

                for(int i=0;i<validPaths.size();i++){
                    if(alreadyVisited.find(validPaths[i]) == alreadyVisited.end()){
                        alreadyVisited.insert(validPaths[i]);
                        q.push({validPaths[i],distance+1});
                    }
                }
            }


        }

        int shortestPathBinaryMatrix(vector<vector<int>>& grid) {

            if(grid[0][0] == 1 || grid[grid.size()-1][grid.size()-1] == 1){
                return -1;
            }

            finalNode = {grid.size()-1,grid.size()-1};
            graph = grid;

            depthFirstSearch();
            
            
            return pathLength;
        }

        vector<pair<int,int>> getValidPathsForNode(pair<int,int> node){

            vector<pair<int,int>> paths;

            int x = node.first;
            int y = node.second;

            // right
            if(y+1<=finalNode.second && graph[x][y+1] == 0){
                paths.push_back({x,y+1});
            }

            // left
            if(y-1>=0 && graph[x][y-1] == 0){
                paths.push_back({x,y-1});
            }

            // bot
            if(x+1 <= finalNode.first && graph[x+1][y] == 0){
                paths.push_back({x+1,y});
            }

            // top
            if(x-1 >= 0 && graph[x-1][y] == 0){
                paths.push_back({x-1,y});
            }

            // diagonal bottom right
            if(x+1 <= finalNode.first && y+1 <= finalNode.second && graph[x+1][y+1] == 0){
                paths.push_back({x+1,y+1});
            }

            // diagonal bottom left
            if(x+1 <= finalNode.first && y-1 >= 0 && graph[x+1][y-1] == 0){
                paths.push_back({x+1,y-1});
            }

            // diagonal top left
            if(x-1 >= 0 && y-1 >= 0 && graph[x-1][y-1] == 0){
                paths.push_back({x-1,y-1});
            }

            // diagonal top right
            if(x-1 >= 0 && y+1 <= finalNode.second && graph[x-1][y+1] == 0){
                paths.push_back({x-1,y+1});
            }
            

            return paths;
            
        }

    private:
        unordered_set<pair<int, int>,pair_hash> alreadyVisited;
        vector<vector<int>> graph;
        pair<int,int> finalNode;
        int pathLength = -1;
};

int main(){

    Solution solution;

    vector<vector<int>> input =  {{0,1,1,0,0,0},{0,1,0,1,1,0},{0,1,1,0,1,0},{0,0,0,1,1,0},{1,1,1,1,1,0},{1,1,1,1,1,0}};

    int answer = solution.shortestPathBinaryMatrix(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}