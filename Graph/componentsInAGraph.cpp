#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<stack>



using namespace std;


int traverseGraphComponent(unordered_map<int,vector<int>> graph,int startNode,unordered_set<int>& alreadyVisited){

    stack<int> stack;
    int counter = 1;

    stack.push(startNode);
    alreadyVisited.insert(startNode);

    while(stack.size()>0){

        int current = stack.top();

        stack.pop();

        for(int i=0;i<graph[current].size();i++){
            if(alreadyVisited.find(graph[current][i]) == alreadyVisited.end()){
                counter++;
                stack.push(graph[current][i]);
                alreadyVisited.insert(graph[current][i]);
            }
        }
    }

    return counter;

}


void printGraph(unordered_map<int,vector<int>> graph){
    for (auto x : graph){

        cout << x.first << " -> ";

        for(int i=0; i<x.second.size();i++){
            cout << " " << graph[x.first][i] << " ";
        }   

        cout << endl;

   }
}


vector<int> componentsInGraph(vector<vector<int>> gb) {

    unordered_map<int,vector<int>> graph;

    for(int i=0;i<gb.size();i++){
        vector<int> edge = gb[i];
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    printGraph(graph);

    unordered_set<int> alreadyVisited;
    vector<int> answer;
    unordered_set<int> counterSet;

   for (auto x : graph){

       int counter = traverseGraphComponent(graph,x.first,alreadyVisited);

        if(counter>1 && counterSet.find(counter) == counterSet.end()){
            answer.push_back(counter);
            counterSet.insert(counter);
        }

   }

    return answer;

    
}




int main(){

    vector<vector<int>> bg = {{1, 17},{5, 13}, {7, 12}, {5,17}, {5, 12},{2,17},{1,18},{8,13},{2,15},{5,20}};

    vector<int> answer;
    answer = componentsInGraph(bg);

    cout << " [ ";

    for(int i=0;i<answer.size();i++){
        cout << " " << answer[i] << " ";
    }
    cout << " ]" << endl;

    return 0;

}