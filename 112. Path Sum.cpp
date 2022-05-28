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

        void depthFirstSearch(TreeNode* node, int sum){

            if(node->left == nullptr && node->right == nullptr){
                sum+= node->val;
                if(sum == target){
                    found = true;
                }
            }

            if(node->left){
                depthFirstSearch(node->left,sum+node->val);
            }

            if(node->right){
                depthFirstSearch(node->right,sum+node->val);
            }

        }

        bool hasPathSum(TreeNode* root, int targetSum) {

            if(!root){
                return false;
            }
            
            target = targetSum;

            depthFirstSearch(root,0);

            return found;          
        }

    private:  
        int target;
        bool found = false;
};

int main(){

    Solution solution;

    TreeNode* root = new TreeNode(5);
    TreeNode* n2 = new TreeNode(4);
    TreeNode* n3 = new TreeNode(11);
    TreeNode* n4 = new TreeNode(7);
    TreeNode* n5 = new TreeNode(2);
    TreeNode* n6 = new TreeNode(8);
    TreeNode* n7 = new TreeNode(13);
    TreeNode* n8 = new TreeNode(4);
    TreeNode* n9 = new TreeNode(1);


    root->left = n2;
    root->right = n6;

    n2->left = n3;
    n3->left = n4;
    n3->right = n5;

    n6->left = n7;
    n6->right = n8;

    n8->right = n9;

    bool answer = solution.hasPathSum(root,22);

    cout << "Answer: " << answer << endl;
    
    
}