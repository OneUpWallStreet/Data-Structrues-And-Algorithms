#include<vector>
#include<iostream>

using namespace std;




//   Definition for a binary tree node.
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

        void replaceWithDFS(TreeNode* node){
            if(node->left || node->right){
                
                TreeNode* temp = node->left;
                node->left = node->right;
                node->right = temp;

                if(node->left){
                    replaceWithDFS(node->left);
                }
                if(node->right){
                    replaceWithDFS(node->right);
                }
            }

        }        

        TreeNode* invertTree(TreeNode* root) {

            if(!root){
                return root;
            }

            replaceWithDFS(root);
            return root;

            
        }
};

int main(){

    // [1,2]

    return 0;
}