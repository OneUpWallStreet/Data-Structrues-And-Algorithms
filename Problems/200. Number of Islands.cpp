#include<iostream>
#include<vector>
#include<unordered_set>
#include<stack>

using namespace std;

// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3
 

// Constraints:

// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 300
// grid[i][j] is '0' or '1'.


struct GridDimensions {
    int row;
    int col;
};

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

class Solution {
    
    public:
        
        void depthFirstTraversal(vector<vector<char>>& grid,int startNode, int endNode){

            stack<pair<int,int>> s;

            // Only go forward if isVisited == false

            if(alreadyVisited.find({startNode,endNode}) != alreadyVisited.end()){
                // cout << "Rejecting : " << startNode << " and  " << endNode << endl;
                return;
            }
            
            s.push({startNode,endNode});

            // cout << "incrmene t for count: " << startNode << " and " << endNode << endl;

            islandCount += 1;

            while(s.size()>0){
                

                int x = s.top().first;
                int y = s.top().second;



                s.pop();

                // Can go above
                if(x-1>=0 && alreadyVisited.find({x-1,y}) == alreadyVisited.end()){
                    if(grid[x-1][y] == '1'){
                        alreadyVisited.insert({x-1,y});
                        s.push({x-1,y});
                    }
                }

                // below
                if(x+1<dimensions.row && alreadyVisited.find({x+1,y}) == alreadyVisited.end()){
                    if(grid[x+1][y] == '1'){
                        alreadyVisited.insert({x+1,y});
                        s.push({x+1,y});
                    }
                }

                // go left
                if(y-1>=0 && alreadyVisited.find({x,y-1}) == alreadyVisited.end()){
                    if(grid[x][y-1] == '1'){
                        alreadyVisited.insert({x,y-1});
                        s.push({x,y-1});
                    }
                }

                // go right
                if(y+1<dimensions.col && alreadyVisited.find({x,y+1}) == alreadyVisited.end()){
                    if(grid[x][y+1] == '1'){
                        alreadyVisited.insert({x,y+1});
                        s.push({x,y+1});
                    }
                }

            }


        }

        int numIslands(vector<vector<char>>& grid) {

            dimensions.row = grid.size();
            dimensions.col = grid[0].size();

            for(int i=0;i<grid.size();i++){
                for(int j=0;j<grid[i].size();j++){
                    if(grid[i][j] == '1') {
                        depthFirstTraversal(grid,i,j);
                    }
                }
            }

            return islandCount;
 
        }

        void printIsland(vector<vector<char>>& grid){
           for(int i=0;i<grid.size();i++){
                for(int j=0;j<grid[i].size();j++){
                    cout << " (" << i << " " << j << " ) ";
                }

                cout << endl;
            }
        }


    private:
        unordered_set< pair<int, int>,  pair_hash> alreadyVisited;
        int islandCount = 0;
        GridDimensions dimensions;

};

int main(){

    Solution solution;

    vector<vector<char>> input = {
        {'1','1','1'},
        {'0','1','0'},
        {'1','1','1'}
    };

    int answer =  solution.numIslands(input);
    cout << "Answer: " << answer << endl;

    return 0;
}