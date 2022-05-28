#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<stack>
#include<iostream>

using namespace std;

class Solution {
    public:

        void depthFirstSearch(int startNode,int n){

            stack<pair<int,int>> s;

            s.push({startNode,0});
            nodesVisited++;

            unordered_set<int> alreadyVisited;

            while(s.size()>0){

                int currentNode = s.top().first;
                int weight = s.top().second;

                if(nodesVisited >= n){
                    time = weight;
                    cout << "time: " << time << endl;

                }

                s.pop();

                for(int i=0;i<graph[currentNode].size();i++){
                    if(alreadyVisited.find(graph[currentNode][i].first) == alreadyVisited.end()){
                        alreadyVisited.insert(currentNode);
                        s.push({graph[currentNode][i].first,weight+graph[currentNode][i].second});
                        nodesVisited++;
                    }
                }

            }

        }

        int networkDelayTime(vector<vector<int>>& times, int n, int k) {

            for(int i=0;i<times.size();i++){
                graph[times[i][0]].push_back({times[i][1],times[i][2]});
            }

            depthFirstSearch(k,n);

            if(nodesVisited < n){
                return -1;
            }


            
            return time;
        }

    private:
    //  First Node, Than Weight
        unordered_map<int,vector<pair<int,int>>> graph;
        int nodesVisited = 0;
        int time = -1;


};




int main(){

    Solution solution;

// [[1,2,1],[2,3,2],[1,3,2]]
// 3
// 1
    

    // Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    // vector<vector<int>> input = {{1,2,1},{2,3,2},{1,3,2}};
    vector<vector<int>> input = {{1,2,1},{2,3,2},{1,3,4}};
// 3
// 1
    // vector<vector<int>> input = {{2,1,1},{2,3,1},{3,4,1}};

    int answer = solution.networkDelayTime(input,3,1);

    cout << "answer is: " << answer << endl;

    return 0;
}


