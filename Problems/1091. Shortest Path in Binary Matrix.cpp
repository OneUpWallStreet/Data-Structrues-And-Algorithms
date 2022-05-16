#include<vector>
#include<stack>
#include<unordered_set>
#include<stack>
#include<iostream>

using namespace std;

struct pair_hash {
    inline size_t operator()(const pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

class Solution {
    public:

        void depthFirstSearch(){

            pair<int,int> node = {0,0};
            alreadyVisited.insert(node);


            stack<pair<pair<int,int>,int>> s;

            s.push({node,1});

            while(s.size()>0){

                int x = s.top().first.first;
                int y = s.top().first.second;

                int distance = s.top().second;

                cout << "visited node: { " << x << " , " << y << " }" << endl;

                if( s.top().first == finalNode){
                    cout << "Final Node Found" << endl;
                    cout << "distance: " << distance << endl;
                    // break;
                }
                

                s.pop();

                vector<pair<int,int>> validPaths = getValidPathsForNode({x,y}); 

                for(int i=0;i<validPaths.size();i++){
                    if(alreadyVisited.find(validPaths[i]) == alreadyVisited.end()){
                        alreadyVisited.insert(validPaths[i]);
                        s.push({validPaths[i],distance+1});
                    }
                }
            }


        }

        int shortestPathBinaryMatrix(vector<vector<int>>& grid) {

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
            if(y+1<=finalNode.second && graph[x][y] == 0){
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

    vector<vector<int>> input =  {{0,0,0},{1,1,0},{1,1,0}};

    int answer = solution.shortestPathBinaryMatrix(input);

    cout << "Answer is: " << answer << endl;


    return 0;
}