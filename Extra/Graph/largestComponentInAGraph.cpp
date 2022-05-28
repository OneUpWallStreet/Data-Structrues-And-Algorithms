#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<stack>



using namespace std;



class Solution{



    public: 

        Solution(unordered_map<int,vector<int>> inputGraph){
            graph = inputGraph;
        }

        int findLargestComponent(){
            int largestCount = 0;
            for(auto x : graph){
                int componentCount = depthFirstTraversal(x.first);
                // cout << "component Count: " << componentCount << endl;
                if(componentCount>largestCount){
                    largestCount = componentCount;
                }
            }
            return largestCount;

        }


    private:
        unordered_set<int> visited;
        unordered_map<int,vector<int>> graph;

        // int depthFirstTraversal(int node,int counter){

        //     if(graph[node].size()==0){
        //         return counter;
        //     }

        //     visited.insert(node);
        //     for(int i=0;i<graph[node].size();i++){
        //         if(visited.find(graph[node][i])==visited.end()){
        //             return depthFirstTraversal(graph[node] [i],counter+1);
        //         }
        //     }

        // }

        int depthFirstTraversal(int node){

            if(visited.find(node) != visited.end()){
                return 0;
            }

            visited.insert(node);

            int size = 1;

            for(int i=0;i<graph[node].size();i++){
                size += depthFirstTraversal(graph[node][i]);
            }

            return size;

        }


};

void printGraph(unordered_map<int,vector<int>> graph){
    for (auto x : graph){
        cout << x.first << " -> ";
        for(int i=0; i<x.second.size();i++){
            cout << " " << graph[x.first][i] << " ";
        }   
        cout << endl;
   }
}

int main(){

    unordered_map<int,vector<int>> graph;

    graph[0] = {8,1,5};
    graph[1] = {0};
    graph[5] = {0,8};
    graph[8] = {0,5};
    graph[2] = {3,4};
    graph[3] = {2,4};
    graph[4] = {3,2};

    Solution solution(graph);

    int answer = solution.findLargestComponent();

    cout << answer << endl;

    // printGraph(graph);


    
}