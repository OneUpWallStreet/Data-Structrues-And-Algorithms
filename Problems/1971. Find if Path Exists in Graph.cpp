#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<stack>

// There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
//  The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a 
// bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, 
// and no vertex has an edge to itself.

// You want to determine if there is a valid path that exists from vertex source to vertex destination.

// Given edges and the integers n, source, and destination, return true if there is a valid path from 
// source to destination, or false otherwise.


// Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
// Output: true
// Explanation: There are two paths from vertex 0 to vertex 2:
// - 0 → 1 → 2
// - 0 → 2

// Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
// Output: false
// Explanation: There is no path from vertex 0 to vertex 5.

// Constraints:

//     1 <= n <= 2 * 105
//     0 <= edges.length <= 2 * 105
//     edges[i].length == 2
//     0 <= ui, vi <= n - 1
//     ui != vi
//     0 <= source, destination <= n - 1
//     There are no duplicate edges.
//     There are no self edges.

using namespace std;
class Solution {
    public:


        bool depthFirstTraversal(int source,int destination){

            stack<int> stack;
            unordered_set<int> visited;
            visited.insert(source); 
            stack.push(source);

            while(stack.size() > 0){
                int current = stack.top();
                if(current == destination){
                    return true;
                }
                stack.pop();
                unordered_set<int> :: iterator itr;
                for(itr = graph[current].begin(); itr != graph[current].end(); itr++){
                    if(visited.find(*itr) == visited.end()){
                        visited.insert(*itr);
                        stack.push(*itr);
                    }                    
                }
            }

            return false;

        }

        void printGraph(){
               for (auto x : graph){
                    unordered_set<int> :: iterator itr;
                    cout << " " <<  x.first <<  "  ";
                    for(itr = x.second.begin();itr != x.second.end();itr++){
                        cout << " " << *itr << " ";
                    }
                    cout << endl; 
               }
        }

        bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
            
            for(int i=0;i<edges.size();i++){
                vector<int> edge = edges[i];
                graph[edge[0]].insert(edge[1]);
                graph[edge[1]].insert(edge[0]);
            }

            return depthFirstTraversal(source,destination);



        }

    private:
        unordered_map<int,unordered_set<int>> graph;
    
    
        

};

int main(){

    Solution solution;

    vector<vector<int>> edges ={{0,1},{1,2},{2,0}};
    bool answer = solution.validPath(3,edges,0,5);

    cout << "Answer: " << answer << endl;

}