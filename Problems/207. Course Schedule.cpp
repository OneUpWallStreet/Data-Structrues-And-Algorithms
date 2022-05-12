#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<vector>

using namespace std;


class Solution {
    public:

        bool dfs(int course){
            
            if(alreadyVisited.find(course) != alreadyVisited.end()){
                return false;
            }

            if(graph[course].size()==0){
                return true;
            }

            alreadyVisited.insert(course);
            for(int i=0;i<graph[course].size();i++){
                if(dfs(graph[course][i])==false){
                    return false;
                }
            }

            alreadyVisited.erase(alreadyVisited.find(course));

            graph[course] = {};
            return true;

        }

        bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
            
            for(int i=0;i<prerequisites.size();i++){
                graph[prerequisites[i][0]].push_back(prerequisites[i][1]);
            }

            for(int i=0;i<numCourses;i++){
                if(dfs(i)==false){
                    return false;
                }
            }

            return true;

        }

    private: 
        unordered_map<int,vector<int>> graph;
        unordered_set<int> alreadyVisited;
};

int main(){

    Solution solution;


    return 0;
}