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

        void depthFirstTraversal(TreeNode* node){
            
            if(!node){
                return;
            }

            // init empty heap & do the work
            treeValues.push_back(node->val);

            depthFirstTraversal(node->left);
            depthFirstTraversal(node->right);


        }

        int kthSmallest(TreeNode* root, int k) {
            
            depthFirstTraversal(root);

            sort(treeValues.begin(),treeValues.end());

            for(int i=0;i<treeValues.size();i++){
                if(i==k-1){
                    return treeValues[i];
                }
            }

            return -1;
        }

    private: 
        vector<int> treeValues;
        int depth = 0;
};

int main(){

    TreeNode* root = new TreeNode(3);
    root->right = new TreeNode(4);
    TreeNode* n2 = new TreeNode(1);
    n2->right = new TreeNode(2);
    root->left = n2;

    Solution solution;

    int answer = solution.kthSmallest(root,1);

    cout << "Answer is: " << answer << endl;





    return 0;
}

