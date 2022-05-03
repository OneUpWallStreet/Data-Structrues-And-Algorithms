#include<iostream>
#include<vector>

using namespace std;

// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

// Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

// Input: n = 4
// Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
// Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

// Example 2:

// Input: n = 1
// Output: [["Q"]]

 

// Constraints:

//     1 <= n <= 9



class Solution {
    

    public:

        Solution(int n){
                        
            N_Value = n;
            vector<vector<int>> vec( n , vector<int> (n, 0));
            board = vec;

        }

        void printBoard(){
            cout << "   _____________________\n_" << endl;

            for(int i=0;i<N_Value;i++){

                for(int j =0; j<N_Value;j++){
                    if(board[i][j]==0){
                        cout << " | " << "."<< " | ";
                    }
                    else{
                        cout << " | " << "Q" << " | ";
                    }
                }

                cout  << "\n   ______________________\n" << endl;

                // cout << endl;
            }

        }

        void place(int row,int col){
            board[row][col] = 1;
        }

        bool isValid(int rowNumber,int colNumber){

            int i,j;
                
            vector<int> row = board[rowNumber];


            // Check if queen exists horizontally
            for(i=0;i<N_Value;i++){
                if(row[i] != 0){
                    return false;
                }
            }

            // Check if queen exists vertically
            for(i=0;i<N_Value;i++){
                if(board[i][colNumber] != 0){
                    return false;
                }
            }


            for(i=rowNumber,j=colNumber;i>=0 && j>=0;i--,j--){
                if(board[i][j]!=0){
                    return false;
                }
            }

            for(i=rowNumber,j=colNumber;i<N_Value && j>=0 ;i++,j--){
                if(board[i][j]!=0){
                    return false;
                }
            }

            for(i=rowNumber,j=colNumber;i>=0 && j<N_Value;i--,j++){
                if(board[i][j]!=0){
                    return false;
                }
            }

            for(i=rowNumber,j=colNumber;i<N_Value && j<=0;i--,j++){
                if(board[i][j]!=0){
                    return false;
                }
            }
                
            return true;
        }


        bool solve(int col){

            if(col>=N_Value){
                return true;
            }

            for(int i=0;i<N_Value;i++){
                if(isValid(i,col)){
                    
                    board[i][col] = 1;

                    if(solve(col+1)){
                        return true;
                    }
                    else{
                        board[i][col] = 0;
                    }
                }
            }
            return false;
            
        }

        vector<vector<string>> solveNQueens(int n) {

            vector<vector<string>> dog;
            return dog;
        }

    private:

        int N_Value;
        vector<vector<int>> board;
        
        

};

int main(){
    Solution solution(4);
    solution.solve(0);
    solution.printBoard();
}