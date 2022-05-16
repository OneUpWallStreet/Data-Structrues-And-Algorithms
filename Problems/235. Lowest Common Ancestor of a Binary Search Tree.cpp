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

        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

            TreeNode* cur = root;

             while(true){

                if(p->val > cur->val && q->val > cur->val){
                    cur = cur->right;
                }
                else if(p->val < cur->val && q->val < cur->val){
                    cur = cur->left;
                }
                else{
                    return cur;
                }
             }
        }
};




int main(){
    Solution solution;

    TreeNode* root = new TreeNode(6);

    TreeNode* n2 = new TreeNode(2);
    TreeNode* n3 = new TreeNode(0);
    TreeNode* n4 = new TreeNode(4);
    TreeNode* n5 = new TreeNode(3);
    TreeNode* n6 = new TreeNode(5);

    TreeNode* n7 = new TreeNode(8);
    TreeNode* n8 = new TreeNode(7);
    TreeNode* n9 = new TreeNode(9);


    root->left = n2;

    n2->left = n3;
    n2->right = n4;

    n4->left = n5;
    n4->right = n6;

    root->right = n7;

    n7->left = n8;
    n7->right = n9;

    TreeNode* answer = solution.lowestCommonAncestor(root,n2,n7);

    cout << "Answer: " << answer->val << endl;

    return 0;
}



    //    vector<int> depthFirstSearch(TreeNode* node, TreeNode* toFind){

    //         stack<TreeNode*> s;
    //         vector<int> path;
    //         s.push(node);
            
    //         while(s.size()>0){

    //             TreeNode* cur = s.top();


    //             if(cur == toFind){
    //                 return path;
    //             }

    //             s.pop();

                
    //             if(cur->left){
    //                 path.push_back(cur->val);
    //                 s.push(cur->left);
    //             }

    //             if(cur->right){
    //                 path.push_back(cur->val);
    //                 s.push(cur->right);
    //             }


    //         }

    //         return path;
    //     }