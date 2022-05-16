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


        bool isSameTreeIterative(TreeNode* p, TreeNode* q){

            stack<pair<TreeNode*,TreeNode*>> s;

            s.push({p,q});

            while(s.size()>0){

                TreeNode* p_cur = s.top().first;
                TreeNode* q_cur = s.top().second;

                s.pop();

                if(p_cur && q_cur && p_cur->val == q_cur->val){
                    s.push({p_cur->left,q_cur->left});
                    s.push({p_cur->right,q_cur->right});
                }
                else if (p_cur || q_cur){
                    return false;
                }
                

            }
            return true;   

        }

        bool isSameTreeRecursive(TreeNode* p, TreeNode* q){
            if(!p && !q){
                return true;
            }
            if(!p || !q || p->val != q->val){
                return false;
            }

            return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
            
        }


        bool isSameTree(TreeNode* p, TreeNode* q) {
            // return isSameTreeRecursive(p,q);
            return isSameTreeIterative(p,q);
        }

};

int main(){

    Solution solution;

    // TreeNode* p_root = new TreeNode(1);
    // TreeNode* q_root = new TreeNode(1);


    // p_root->left = new TreeNode(2);

    // q_root->right = new TreeNode(2);


    TreeNode* p_root = new TreeNode(1);
    TreeNode* p2 = new TreeNode(2);
    TreeNode* p3 = new TreeNode(3);

    p_root->left = p2;
    p_root->right = p3;

    TreeNode* q_root = new TreeNode(1);
    TreeNode* q2 = new TreeNode(2);
    TreeNode* q3 = new TreeNode(3);

    q_root->left = q2;
    q_root->right = q3;
    
    bool answer = solution.isSameTree(p_root,q_root);

    cout << "Answer: " << answer << endl;


}