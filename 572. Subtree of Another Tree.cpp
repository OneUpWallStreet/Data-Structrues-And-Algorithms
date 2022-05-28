#include<vector>
#include<iostream>
#include<stack>

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

        bool checkForSubtree(TreeNode* root, TreeNode* subRoot){
            
            if(!root && !subRoot){
                return true;
            }

            if(!root || !subRoot || root->val != subRoot->val){
                return false;
            }

            return checkForSubtree(root->left,subRoot->left) && checkForSubtree(root->right,subRoot->right);

        }


        bool isSubtree(TreeNode* root, TreeNode* subRoot) {
            // Perform dfs till value is same than call subtree
                
            stack<TreeNode*> s;

            s.push(root);

            while(s.size()>0){
                
                TreeNode* cur = s.top();

                s.pop();

                if(cur->val == subRoot->val){
                    if(checkForSubtree(cur,subRoot)){
                        return true;
                    }
                }

                if(cur->left){
                    s.push(cur->left);
                }

                if(cur->right){
                    s.push(cur->right);
                }

            }
            
            return false;
        }
};

int main(){

    Solution solution;

    TreeNode* root = new TreeNode(3);
    root->right = new TreeNode(5);
    

    TreeNode* main_2 = new TreeNode(4);
    main_2->left = new TreeNode(1);
    main_2->right = new TreeNode(2);

    TreeNode* subTreeRoot = new TreeNode(4);

    subTreeRoot->left = new TreeNode(1);
    subTreeRoot->right = new TreeNode(2);

    root->left = main_2;


     bool answer = solution.isSubtree(root,subTreeRoot);

    cout << "Answer: " << answer << endl;

}
