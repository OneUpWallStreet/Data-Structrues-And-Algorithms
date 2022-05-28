#include<vector>
#include<iostream>


using namespace std;


 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

struct BalanceTreeStruct {
    bool isBalanced;
    int height;
};

class Solution {
    public:

        BalanceTreeStruct depthFirstSearch(TreeNode* node){

            if(!node){
                return {true,0};
            }

            BalanceTreeStruct left = depthFirstSearch(node->left);
            BalanceTreeStruct right = depthFirstSearch(node->right);

            bool balanced = false;

            if(left.isBalanced == true && right.isBalanced == true && abs(left.height - right.height) <= 1){
                balanced = true;
            }

            return {balanced,1+ max(left.height,right.height)};

        }

        bool isBalanced(TreeNode* root) {
            return depthFirstSearch(root).isBalanced;
        }
};


int main(){

    Solution solution;

    TreeNode* root = new TreeNode(3);

    TreeNode* n2 = new TreeNode(9);
    TreeNode* n3 = new TreeNode(20);
    TreeNode* n4 = new TreeNode(15);
    TreeNode* n5 = new TreeNode(7);

    root->left = n2;

    root->right = n3;

    n3->left = n4;
    n3->right = n5;

    bool answer = solution.isBalanced(root);

    cout << "Answer: " << answer << endl;
    return 0;
}