#include<iostream>
#include<vector>

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

        void calculateDepthOfTree(TreeNode* node,int currentDepth){

                // check if this is a leaf node
                if(node->left == nullptr && node->right == nullptr){
                    // We mark this as depth of tree, only if it's greater
                    // than older depth
                    depth = max(depth,currentDepth);
                    return;
                }

                // continue dfs on left and right nodes 
                // (if they exist)

                if(node->left){
                    calculateDepthOfTree(node->left,currentDepth+1);
                }
                if(node->right){
                    calculateDepthOfTree(node->right,currentDepth+1);
                }

            }


        int maxDepth(TreeNode* root) {
            
            if(!root){
                return 0;
            }
            
            calculateDepthOfTree(root,1);
            return depth;
        }
    
    private:
        int depth = 1;
    
    
    
};