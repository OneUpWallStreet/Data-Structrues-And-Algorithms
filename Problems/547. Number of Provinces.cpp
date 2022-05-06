#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

// There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

// A province is a group of directly or indirectly connected cities and no other cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

// Return the total number of provinces.

// Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
// Output: 2

// Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
// Output: 3


// Constraints:

//     1 <= n <= 200
//     n == isConnected.length
//     n == isConnected[i].length
//     isConnected[i][j] is 1 or 0.
//     isConnected[i][i] == 1
//     isConnected[i][j] == isConnected[j][i]



class QuickUnion {

    public: 
        QuickUnion(int n){
            size = n;
            root = new int[size];
            rank = new int[size];
            for(int i=0;i<size;i++){
                root[i] = i;
                rank[i] = 1;
            }
        }

        int find(int x){
            if(root[x] == x){
                return x;
            }
            return root[x] = find(root[x]);
        }

        void unionSet(int x,int y){
            int rootX = find(x);
            int rootY = find(y);

            if(rootX!= rootY){

                if(rank[rootX]>rank[rootY]){
                    root[rootY] = rootX;
                }
                else if(rank[rootX]<rank[rootY]){
                    root[rootX] = rootY;
                }
                else{
                    root[rootX] = rootY;
                    rank[rootY] += 1;
                }
            }
        }

        bool isConnected(int x,int y){
            if(root[x] == root[y]){
                return true;
            }
            return false;
        }

        int countProvince(){

            int counter = 0;

            cout << endl;

            for(int i=0;i<size;i++){
               int rootNode = find(i);
               if(provSet.find(rootNode) == provSet.end()){
                    provSet.insert(rootNode);
                   counter++;
               }               
            }

            return counter;
        }

    private:
        int size;
        int *root;
        int *rank;
        unordered_set<int> provSet;
};


class Solution {
    public:
        int findCircleNum(vector<vector<int>>& isConnected) {
            
            QuickUnion disjointSet(isConnected.size());

            for(int i=0;i<isConnected.size();i++){
                for(int j=0;j<isConnected.size();j++){
                    if(isConnected[i][j]==1){
                        disjointSet.unionSet(i,j);
                    }
                }
            }

            return disjointSet.countProvince();            
        }
};

int main(){ 
    Solution solution;
    vector<vector<int>> input = {{1,1,0},{1,1,0},{0,0,1}};
    int answer = solution.findCircleNum(input);
    cout << "Answer: " << answer << endl;
    return 0;
}