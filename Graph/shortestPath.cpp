#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<queue>

using namespace std;



class Solution {

    public:
        Solution(vector<vector<char>> edges){
            for(int i=0;i<edges.size();i++){
                vector<char> edge = edges[i];
                graph[edge[0]].insert(edge[1]);
                graph[edge[1]].insert(edge[0]);
            }

            printGraph();
        }


        int shortestPath(char startNode,char endNode){
            queue<pair<char,int>> q;

            q.push({startNode,0});
            alreadyVisited.insert(startNode);

            while(q.size()>0){

                char currentNode = q.front().first;
                int currentDistance = q.front().second;

                if(currentNode==endNode){
                    return currentDistance;
                }

                q.pop();

                alreadyVisited.insert(currentNode);

                for(const auto& elem: graph[currentNode]){
                    if(alreadyVisited.find(elem) == alreadyVisited.end()){
                        q.push({elem,currentDistance+1});
                    }
                }
            }

            return -1;
        }


        void printGraph(){
            for (auto x : graph){
                cout << x.first << " -> ";
                for (const auto& elem: x.second) {
                    cout << " " << elem << " ";
                }
                cout << endl;
            }
        }



    private:
        unordered_map<char,unordered_set<char>> graph;
        unordered_set<char> alreadyVisited;

};


int main(){

    vector<vector<char>> edges = { {'w','x'}, {'x','y'},{'z','y'},{'z','v'},{'w','v'} };
    Solution solution(edges);
    int answer = solution.shortestPath('w','z');
    cout << "distance is: " << answer << endl;
    return 0;

}