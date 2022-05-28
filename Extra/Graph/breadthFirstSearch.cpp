#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>

using namespace std;


class GraphBFS {

    public:
        GraphBFS(unordered_map<char,vector<char>> inputGraph){
            graph = inputGraph;
        }

        void IterativeGraphTraversal(char node){

            queue<char> q;
            q.push(node);
            while(q.size()>0){
                char current = q.front();
                q.pop();
                cout << current << endl; 

                for(int i=0;i<graph[current].size();i++){
                    q.push(graph[current][i]);
                }
            }


        }

        void RecursiveGraphTraversal(char node){

            cout << node << endl;



        }

    private:
        unordered_map<char,vector<char>> graph;




};

int main(){


    unordered_map<char,vector<char>> graph;

    graph['a'] = {'c','b'};
    graph['b'] = {'d'};
    graph['c'] = {'e'};
    graph['d'] = {'f'};
    graph['e'] = {};
    graph['f'] = {};

    GraphBFS bfs(graph);

    bfs.IterativeGraphTraversal('a');



    return 0;
}