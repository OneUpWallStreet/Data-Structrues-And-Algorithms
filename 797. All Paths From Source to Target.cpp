#include<iostream>
#include<vector>
#include<unordered_map>
#include<stack>
#include<queue>
using namespace std;


// Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths 
// from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you can visit
//  from node i (i.e., there is a directed edge from node i to node graph[i][j]).

//  Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all 
// possible paths from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you can visit from
//  node i (i.e., there is a directed edge from node i to node graph[i][j]).

// Input: graph = [[1,2],[3],[3],[]]
// Output: [[0,1,3],[0,2,3]]
// Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

// Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
// Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


// Constraints:

// n == graph.length
// 2 <= n <= 15
// 0 <= graph[i][j] < n
// graph[i][j] != i (i.e., there will be no self-loops).
// All the elements of graph[i] are unique.
// The input graph is guaranteed to be a DAG.

class Solution {
    public:

        vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {

            stack<pair<int,vector<int>>> s;

            vector<vector<int>> result;

            int target = graph.size()-1;

            s.push({0,{0}});

            while(s.size()>0){

                int currentNode = s.top().first;
                vector<int> route = s.top().second;

                s.pop();

                if(currentNode == target){
                    result.push_back(route);
                }
                else{
                    for(int i=0;i<graph[currentNode].size();i++){
                        vector<int> nextRoute = route;
                        nextRoute.push_back(graph[currentNode][i]);
                        s.push({graph[currentNode][i],nextRoute});
                    }
                }


            }
            return result;
        }

        void printAnswer(vector<vector<int>> result){
            for(int i=0;i<result.size();i++){
                cout << "First Answer -> ";
                for(int j=0;j<result[i].size();j++){
                    cout << " " << result[i][j] << " ";
                }
                cout << endl;
            }
        }


};



int main(){
    Solution solution;
    vector<vector<int>> input = {{4,3,1},{3,2,4},{3},{4},{}};
    solution.allPathsSourceTarget(input);
}