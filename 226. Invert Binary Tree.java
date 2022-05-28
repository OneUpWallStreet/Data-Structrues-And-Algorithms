class Solution {

    private void recursiveReverseTree(TreeNode node){
        if(node==null){
            return;
        }

        TreeNode temp = node.left;
        node.left = node.right;
        node.right = temp;

        recursiveReverseTree(node.left);
        recursiveReverseTree(node.right);
    }

    public TreeNode invertTree(TreeNode root) {
        recursiveReverseTree(root);
        return root;
    }
}