#include<vector>
#include<iostream>


using namespace std;

//   Definition for a binary tree node.
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
        int deepestLeavesSum(TreeNode* root) {
	
			// We need to find out the depth of the tree first
			// so we only consider those leaf nodes
            calculateDepthOfTree(root,0);
			
			// Recursive DFS func to calculate 
			// sum
            traverseTree(root,0);
            
            return sum;
        }

    private: 

        void calculateDepthOfTree(TreeNode* node,int currentDepth){

			// check if this is a leaf node
            if(node->left == nullptr && node->right == nullptr){
				// We mark this as depth of tree, only if it's greater
				// than older depth
                depth = max(depth,currentDepth);
                return;
            }

			// continue dfs on left and right nodes 
			// (if they exist)
			
            if(node->left){
                calculateDepthOfTree(node->left,currentDepth+1);
            }
            if(node->right){
                calculateDepthOfTree(node->right,currentDepth+1);
            }


        }

		// Recurisve DFS func to calculate sum of deepest leaves
        void traverseTree(TreeNode* node,int currentDepth){

			// only append sum if 
			// 1) this is a leaf node
			// 2) the current depth == total depth of tree ( we 
			//     calculated this in calculateDepthOfTree func )
            if(node->left == nullptr && node->right == nullptr && currentDepth == depth){
                sum += node->val;
                return;
            }

			// continue dfs on left and right nodes 
			// (if they exist)
            if(node->left){
                traverseTree(node->left,currentDepth+1);
            }
            
            if(node->right){
                traverseTree(node->right,currentDepth+1);
            }
        }

        int sum = 0;
        int depth = 0;
};


// [1,2,3,4,5,null,6,7,null,null,null,null,8]



int main(){ 

    Solution solution;

    TreeNode* root = new TreeNode(1);
    TreeNode* n2 = new TreeNode(2);
    TreeNode* n3 = new TreeNode(3);
    TreeNode* n4 = new TreeNode(4);
    TreeNode* n5 = new TreeNode(5);
    TreeNode* n6 = new TreeNode(6);
    TreeNode* n7 = new TreeNode(7);
    TreeNode* n8 = new TreeNode(8);


    root->left = n2;
    root->right = n3;

    n2->left = n4;
    n2->right = n5;

    n4->left = n7;

    n3->right = n6;
    n6->right = n8;

    int answer = solution.deepestLeavesSum(root);

    cout << "Answer is: " << answer << endl;


    return 0;

}