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

        void printVector(vector<int> nums){

            for(int i=0;i<nums.size();i++){
                cout << " " << nums[i] << " ";
            }

            cout << endl;

        }

        void depthFirstSearch(TreeNode* node, int depth){

            result[depth].push_back(node->val);


            if(node->left){
                depthFirstSearch(node->left,depth+1);
            }

            if(node->right){
                cout << "Here" << endl;
                depthFirstSearch(node->right,depth+1);
            }
            
        }

        void findDepthOfTree(TreeNode* node, int currentDepth){
            
            if(node->left == nullptr && node->right == nullptr){
                totalDepth = max(totalDepth,currentDepth);
                return;
            }

            if(node->left){
                findDepthOfTree(node->left,currentDepth+1);
            }

            if(node->right){
                findDepthOfTree(node->right,currentDepth+1);
            }

        }

        vector<vector<int>> levelOrder(TreeNode* root) {

            if(!root){
                return result;
            }

            
            findDepthOfTree(root,1);
            vector<vector<int>> arr(totalDepth);

            result = arr;

            depthFirstSearch(root,0);

            for(int i=0;i<result.size();i++){
                printVector(result[i]);
            }

            return result;

        }
    private:
        int totalDepth = 0;
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


    // solution.levelOrder()

    return 0;
}