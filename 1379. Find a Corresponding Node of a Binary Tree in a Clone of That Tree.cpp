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

        void depthFirstSearch(TreeNode* original, TreeNode* cloned){

            if(original->val == cloned->val && original->val == targetValue){
                targetNode = cloned;
                return;
            }

            if(original->left){
                depthFirstSearch(original->left,cloned->left);
            }

            if(original->right){
                depthFirstSearch(original->right,cloned->right);
            }

        }

        TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
            targetValue = target->val;
            depthFirstSearch(original,cloned);
            return targetNode;
        }

    private: 
        int targetValue;
        TreeNode* targetNode;
    
};

int main(){

    Solution solution;

    TreeNode* root1 = new TreeNode(7);
    root1->left = new TreeNode(4);
    TreeNode* p1 = new TreeNode(3);
    root1->right = p1;
    p1->left = new TreeNode(6);
    p1->right = new TreeNode(19);

    TreeNode* root2 = new TreeNode(7);
    root2->left = new TreeNode(4);
    TreeNode* q1 = new TreeNode(3);
    root2->right = q1;
    q1->left = new TreeNode(6);
    q1->right = new TreeNode(19);

    solution.getTargetCopy(root1,root2,q1);


    return 0;
}
