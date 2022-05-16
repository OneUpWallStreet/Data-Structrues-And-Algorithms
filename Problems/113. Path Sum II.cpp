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

        void depthFirstSearch(TreeNode* node, int currentSum, vector<int> path){

            currentSum = currentSum + node->val;
            
            path.push_back(node->val);
            
            if(node->left == nullptr && node->right == nullptr){
                if(currentSum == target){
                    result.push_back(path);
                }
                return;
            }

            if(node->left){
                depthFirstSearch(node->left,currentSum,path);
            }
            if(node->right){
                depthFirstSearch(node->right,currentSum,path);
            }

        }

        vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
    
            if(!root){
                return result;
            }
            target = targetSum;
            depthFirstSearch(root,0,{});
            return result;
        }
    
    private: 
        int target;
        vector<vector<int>> result;
};

int main(){

    Solution solution;

    TreeNode* root = new TreeNode(5);

    TreeNode* n2 = new TreeNode(4);
    TreeNode* n3 = new TreeNode(8);
    TreeNode* n4 = new TreeNode(11);
    TreeNode* n5 = new TreeNode(7);
    TreeNode* n6 = new TreeNode(2);
    TreeNode* n7 = new TreeNode(13);
    TreeNode* n8 = new TreeNode(4);
    TreeNode* n9 = new TreeNode(5);
    TreeNode* n10 = new TreeNode(1);

    root->left = n2;
    root->right = n3;

    n2->left = n4;
    n4->left = n5;
    n4->right = n6;

    n3->left = n7;
    n3->right = n8;
    
    n8->left = n9;
    n8->right = n10;

    vector<vector<int>> answer = solution.pathSum(root,22);

    cout << "Size: " << answer.size() << endl;

    
    return 0;
}