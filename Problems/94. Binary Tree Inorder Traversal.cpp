#include<vector>
#include<stack>
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

        void recursiveSoln(TreeNode* root){

            if(root){
                if(root->left){
                        recursiveSoln(root->left);
                    }
                    
                    result.push_back(root->val);

                    if(root->right){
                        recursiveSoln(root->right);
                    }

                }
        }

        vector<int> inorderTraversal(TreeNode* root) {
            recursiveSoln(root);
            return result;
        }

    private: 
        vector<int> result;
};

// Input: root = [1,null,2,3]


int main(){

    TreeNode* t1 = new TreeNode(1);
    TreeNode* t2 = new TreeNode(2);
    TreeNode* t3 = new TreeNode(3);

    t1->left = nullptr;
    t1->right = t2;
    t2->left = t3;

    Solution solution;

    // vector<int> answer = solution.inorderTraversal(t1);
    
    vector<int> answer = solution.iterativeSolution(t1);

    for(int i=0;i<answer.size();i++){
        cout << " " << answer[i] << " ";
    }

    cout << endl;

    // solution.iterativeSolution(t1);
    
    cout << "Answer size: " << answer.size() << endl;
    return 0;
}