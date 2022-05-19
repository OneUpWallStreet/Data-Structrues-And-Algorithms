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

class Solution {
    public:

        bool depthFirstTraversal(TreeNode* node, int cutOff){

            if(!node){
                return true;
            }

            // cout << "node val: " << node->val << endl;
            // cout << "node->right->val" << node->right->val << endl;
//            cout << "node->left->val: " << node->left->val << endl;

            if(node->left && node->right && node->left->val >= node->right->val){
                return false;
            }  
            if(node->left && (node->left->val >= node->val || node->left->val >= cutOff)){
                return false;
            }
            if(node->right && (node->val >= node->right->val || node->right->val <= cutOff)){
                return false;
            }
            


            // if(node->left != nullptr && node->right != nullptr){
            //     if(node->left->val >= node->right->val || node->left->val >= node->val || node->val >= node->right->val){
            //         return false;
            //     }   
            // }




            return (depthFirstTraversal(node->left,cutOff) && depthFirstTraversal(node->right,cutOff));
            


        }

        bool isValidBST(TreeNode* root) {
            return depthFirstTraversal(root,root->val);
            // return false;
        }
};


int main(){

    Solution solution;

    // TreeNode* root = new TreeNode(1);

    // root->left = new TreeNode(1);



    TreeNode* root = new TreeNode(5);

    root->left = new TreeNode(1);

    TreeNode* n2 = new TreeNode(4);

    root->right = n2;

    n2->left = new TreeNode(3);
    n2->right = new TreeNode(7);

    bool answer = solution.isValidBST(root);

    cout << "answer: " << answer << endl;

}