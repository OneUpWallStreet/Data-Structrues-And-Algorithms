#include<iostream>
#include<unordered_set>
#include<vector>
#include<stack>
#include<queue>

using namespace std;

// Given an m x n grid of characters board and a string word, return true if word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
// are horizontally or vertically neighboring. The same letter cell may not be used more than once.

// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true


// ["A","B","C","E"]
// ["S","F","C","S"]
// ["A","D","E","E"]


struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

struct GridDimensions {
    int row;
    int col;
};


class Solution {
    public:
    
        bool exist(vector<vector<char>>& board, string word) {
            
            boardDimensions.row = board.size();
            boardDimensions.col = board[0].size();
            mainWord = word;

            for(int i =0;i<boardDimensions.row;i++){
                for(int j=0;j<boardDimensions.col;j++){
                    if(depthFirstRecursive(board,0,i,j)){
                        return true;
                    }
                }
            }

            return false;


        }
    private:

        bool depthFirstRecursive(vector<vector<char>>& board,int i, int x, int y){

            if(i == mainWord.length()){
                return true;
            }
            
            if(x<0 || x>= boardDimensions.row){
                return false;
            }

            if(y<0 || y>= boardDimensions.col){
                return false;
            }

            if(board[x][y] == '$'){
                return false;
            }

            if(mainWord[i] != board[x][y]){
                return false;
            }

            char oldValue = board[x][y];
            board[x][y] = '$';


            if(depthFirstRecursive(board,i+1,x+1,y) || depthFirstRecursive(board,i+1,x-1,y) || depthFirstRecursive(board,i+1,x,y-1) || depthFirstRecursive(board,i+1,x,y+1)){
                return true;
            }

            board[x][y] = oldValue;


            return false;
        }

  
        GridDimensions boardDimensions;
        string mainWord;
        


};




int main(){
    Solution solution;
    vector<vector<char>> input = {{'C','A','A'}, {'A','A','A'},{'B','C','D'}};
    bool answer = solution.exist(input,"AAB");
    cout << "Answer is:  " << answer << endl; 
}