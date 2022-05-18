#include<vector>
#include<unordered_map>
#include<stack>
#include<unordered_set>
#include<set>
#include<iostream>

using namespace std;


class Solution {
    public:

        void depthFirstSearch(int node){
            stack<pair<int,vector<int>>> s;
            // stack<pair<int,vec
            
            unordered_set<int> alreadyVisited;

            s.push({node,{node}});
            alreadyVisited.insert(node);

            while(s.size()>0){

                int current = s.top().first;
                vector<int> path = s.top().second;

                // printVector(path);

                s.pop();

                if(alreadyVisited.find(current) != alreadyVisited.end()){
                    cycleEdges.insert(current);
                }

                vector<int> edges = graph[current];

                if(edges.size() == 0){

                    if(path.size()>1){
                        int ele1 = path.back();
                        path.pop_back();
                        int ele2 = path.back();
                        path.pop_back();
                        vector<int> ans = {ele1,ele2};

                        sort(ans.begin(),ans.end());

                        if(alreadySeenEdges.find(ans) == alreadySeenEdges.end()){
                            result.push_back(ans);
                            alreadySeenEdges.insert(ans);
                        }
                        
                        // printVector(ans);
                    }

                }

                for(int i=0;i<edges.size();i++){
                    
                    // Edge not found
                    if(alreadyVisited.find(edges[i]) == alreadyVisited.end()){
                        alreadyVisited.insert(edges[i]);
                        vector<int> nextPath = path;
                        nextPath.push_back(edges[i]);
                        s.push({edges[i],nextPath});
                    }

                }
            
            }



        }

        void printVector(vector<int> nums){

            for(int i=0;i<nums.size();i++){
                cout << " " << nums[i] << " ";
            }

            cout << endl;

        }

        void printGraph(){
            for (auto& it: graph) {
                cout << it.first << " -> ";
                printVector(it.second); 
            }
        }

        vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {

            for(int i=0;i<connections.size();i++){
                if(graph.find(connections[i][0]) == graph.end()){
                    vector<int> adjList;
                    adjList.push_back(connections[i][1]);
                    graph[connections[i][0]] = adjList;
                }
                else{
                    graph[connections[i][0]].push_back(connections[i][1]);
                }
            }

            printGraph();


            for(int i=0;i<n;i++){
                depthFirstSearch(i);
            }

            for(int i=0;i<result.size();i++){
                printVector(result[i]);
            }

            // depthFirstSearch(1);

            vector<int> noCycle;


            for (auto& it: graph) {
                // Found
                if(cycleEdges.find(it.first) == cycleEdges.end()){
                    noCycle.push_back(it.first);
                }
            }




            return result;
        }

    private: 
        unordered_map<int,vector<int>> graph;
        vector<vector<int>> result;
        unordered_set<int> cycleEdges;
        set<vector<int>> alreadySeenEdges;
};


int main(){

    Solution solution;

    // vector<vector<int>> graph = {{0,1},{1,2},{2,0},{1,3}};
    // vector<vector<int>> graph = {{0,1}};
    vector<vector<int>> graph = {{0,1},{1,2},{2,0},{1,3},{3,4},{4,5},{5,3}};

    vector<vector<int>> answer =  solution.criticalConnections(6,graph);

}