import java.util.*;



// Definition for a binary tree node.
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

    List<Integer> result = new ArrayList<>();

    private void depthFirstTraversal(TreeNode node){

        if(node == null){
            return;
        }

        depthFirstTraversal(node.left);
        depthFirstTraversal(node.right);
        result.add(node.val);


    }

    public List<Integer> postorderTraversal(TreeNode root) {
        depthFirstTraversal(root);
        return result;
    }

}