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

        void depthFirstTraversal(TreeNode* node, int maxValue){

            if(node->val >= maxValue){
                goodNodeCount++;
            }

            maxValue = max(maxValue,node->val);
            
            if(node->left){
                depthFirstTraversal(node->left,maxValue);
            }

            if(node->right){
                depthFirstTraversal(node->right,maxValue);
            }

        }

        int goodNodes(TreeNode* root) {
            depthFirstTraversal(root,-100000);
            return goodNodeCount;
        }

    private: 
        int goodNodeCount = 0;
};

int main(){

    Solution solution;

    TreeNode* root = new TreeNode(-1);
    TreeNode* n1 = new TreeNode(1);
    root->left = n1;
    n1->left = new TreeNode(3);

    TreeNode* n2 = new TreeNode(4);

    root->right = n2;

    n2->left = new TreeNode(1);
    n2->right = new TreeNode(5);

    int answer = solution.goodNodes(root);

    cout << "Answer is: " << answer << endl;

}