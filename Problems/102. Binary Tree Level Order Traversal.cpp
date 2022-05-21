#include<vector>
#include<iostream>
#include<queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
    public:

        void breathFirstSearch(TreeNode* node){

            queue<TreeNode*> q;
            q.push(node);

            while(q.size()>0){

                TreeNode* cur = q.front();
                
                q.pop();

                vector<int> curRow;

                if(cur->left){
                    curRow.push_back(cur->left->val);
                    q.push(cur->left);
                }

                if(cur->right){
                    curRow.push_back(cur->right->val);
                    q.push(cur->right);
                }

                result.push_back(curRow);

            }
        }

        vector<vector<int>> levelOrder(TreeNode* root) {
            breathFirstSearch(root);   
            return result;
        }

    private: 
        vector<vector<int>> result;
};

int main(){

    Solution solution;

    TreeNode* root = new TreeNode(3);

    root->left = new TreeNode(9);

    TreeNode* n2 = new TreeNode(20);

    root->right = n2;

    n2->left = new TreeNode(15);
    n2->right = new TreeNode(7);

    vector<vector<int>> answer = solution.levelOrder(root);


    return 0;
}