#include<iostream>
#include<vector>
#include<unordered_map>
#include<stack>

using namespace std;

class GraphDFS{
    
    public: 
        GraphDFS(unordered_map<char,vector<char>> inputGraph){
            graph = inputGraph;
        }

        void RecursiveGraphTraversal(char node){

            cout << node << endl;

            // This case is not needed, becuase if node is empty the for loop will never be executed
            if(graph[node].size()==0){
                return;
            }
            
            for(int i=0;i<graph[node].size();i++){
                RecursiveGraphTraversal(graph[node][i]);
            }

        }

        void IterativeGraphTraversal(char node){

            stack<char> stack;
            stack.push(node);

            while(stack.size() > 0){
                char current = stack.top();
                stack.pop();
                cout <<  current << endl;
                for(int i=0;i<graph[current].size();i++){
                    stack.push(graph[current][i]);
                }            
            }
        }

    private:
        unordered_map<char,vector<char>> graph;
};



int main(){

    unordered_map<char,vector<char>> graph;

    graph['a'] = {'b','c'};
    graph['b'] = {'d'};
    graph['c'] = {'e'};
    graph['d'] = {'f'};
    graph['e'] = {};
    graph['f'] = {};

    GraphDFS dfs(graph);

    // dfs.IterativeGraphTraversal('a');
    dfs.RecursiveGraphTraversal('a');
}

