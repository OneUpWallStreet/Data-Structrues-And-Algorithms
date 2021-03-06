#include<vector>
#include<unordered_set>
#include<iostream>


using namespace std;

class Solution {
    public:


        bool areSubBlocksValid(vector<vector<char>>& board){

            for(int i=0; i< board.size();i+=3){
                for(int j=0;j<board[i].size();j+=3){
                    unordered_set<char> blockSet;

                    for(int x=i;x<i+3;x++){
                        for(int y=j;y<j+3;y++){
                            if(board[x][y] == '.'){
                                continue;
                            }

                            if(blockSet.find(board[x][y]) == blockSet.end()){
                                blockSet.insert(board[x][y]);
                            }
                            else{
                                return false;
                            }
                        }
                    }
                }
            }

            return true;

        }

        bool areRowsValid(vector<vector<char>>& board){
            // Loop through every row
            for(int i=0;i<board.size();i++){
                unordered_set<char> rowSet;
                for(int j=0;j<board[i].size();j++){
                    if(board[i][j] == '.'){
                        continue;
                    }
                    if(rowSet.find(board[i][j])  == rowSet.end()){
                        rowSet.insert(board[i][j]);
                    }
                    else {
                        return false;
                    }
                }
            }

            return true;
        }


        bool areColumnsValid(vector<vector<char>>& board){
            for(int i=0;i<board[0].size();i++){
                unordered_set<char> colSet;
                for(int j=0;j<board.size();j++){
                    if(board[j][i] == '.'){
                        continue;
                    }
                    if(colSet.find(board[j][i]) == colSet.end()){
                        colSet.insert(board[j][i]);
                    }
                    else{
                        return false;
                    }
                }   
            }
            return true;
        }

        bool isValidSudoku(vector<vector<char>>& board) {

            if( areRowsValid(board) == false || areColumnsValid(board) == false || areSubBlocksValid(board) == false){
                return false;
            }
            
            return true;
        }
};

int main(){
    
    Solution solution;

    vector<vector<char>> board = 
    {{'.','.','4','.','.','.','6','3','.'},
    {'.','.','.','.','.','.','.','.','.'},
    {'5','.','.','.','.','.','.','9','.'},
    {'.','.','.','5','6','.','.','.','.'},
    {'4','.','3','.','.','.','.','.','1'},
    {'.','.','.','7','.','.','.','.','.'},
    {'.','.','.','5','.','.','.','.','.'},
    {'.','.','.','.','.','.','.','.','.'},
    {'.','.','.','.','.','.','.','.','.'}};


    bool answer = solution.isValidSudoku(board);    
    cout << "Answer is: " << answer << endl;

    
}