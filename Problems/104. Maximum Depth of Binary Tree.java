// * Definition for a binary tree node.
class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}


class Solution {
    private int depthFirstTraversal(TreeNode node,int currentDepth){
        if(node==null || (node.left == null && node.right == null)){
            return  currentDepth;
        }
        return Math.max(depthFirstTraversal(node.left,currentDepth+1),depthFirstTraversal(node.right,currentDepth+1));
    }

    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        return depthFirstTraversal(root,1);
    }
}
