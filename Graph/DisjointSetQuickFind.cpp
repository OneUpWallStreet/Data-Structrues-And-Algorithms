#include<iostream>

using namespace std;

class QuickFind {

    public:
        QuickFind(int n){
            size = n;
            root = new int[size];
            for(int i=0;i<size;i++){
                root[i] = i;
            }
        }

        int find(int x){
            return root[x];
        }

        void unionSet(int X, int Y){

            int rootX = find(X);
            int rootY = find(Y);

            if(rootX != rootY){
                for(int i=0;i<size;i++){
                    if(root[i] == rootY){
                        root[i] = rootX;
                    }
                }
            }
        }

        bool connected(int X,int Y) {
            if(root[X] == root[Y]){
                return true;
            }
            return false;
        }


    private:
        int size;
        int *root;


};


int main(){
    // for displaying booleans as literal strings, instead of 0 and 1
    cout << boolalpha;
    QuickFind uf(10);
    // 1-2-5-6-7 3-8-9 4
    uf.unionSet(1, 2);
    uf.unionSet(2, 5);
    uf.unionSet(5, 6);
    uf.unionSet(6, 7);
    uf.unionSet(3, 8);
    uf.unionSet(8, 9);
    cout << uf.connected(1, 5) << endl;  // true
    cout << uf.connected(5, 7) << endl;  // true
    cout << uf.connected(4, 9) << endl;  // false
    // 1-2-5-6-7 3-8-9-4
    uf.unionSet(9, 4);
    cout << uf.connected(4, 9) << endl;  // true
    return 0;
}

