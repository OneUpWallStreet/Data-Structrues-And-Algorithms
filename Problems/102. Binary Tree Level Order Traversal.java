import java.util.*;

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

class TreeNodeAndDepth {
    TreeNode node;
    int depth;

    TreeNodeAndDepth(TreeNode node, int depth){
        this.depth = depth;
        this.node = node;
    }
}

class Solution {

    List<List<Integer>> result = new ArrayList<>();
    HashMap<Integer,List<Integer>> map = new HashMap<>();

    private void breathFirstSearch(TreeNode root){

        if(root == null){
            return;
        }

        Queue<TreeNodeAndDepth> queue = new LinkedList<>();

        List<Integer> rootLevel = new ArrayList<>();
        rootLevel.add(root.val);

        map.put(0,rootLevel);

        queue.add(new TreeNodeAndDepth(root,0));

        while(queue.size()>0){

            TreeNodeAndDepth cur = queue.poll();

            if(cur.node.left != null){
                queue.add(new TreeNodeAndDepth(cur.node.left,cur.depth+1));
                List<Integer> curLevel;
                if(map.containsKey(cur.depth+1)){
                    curLevel = map.get(cur.depth + 1);
                }
                else{
                    curLevel = new ArrayList<>();
                }
                curLevel.add(cur.node.left.val);
                map.put(cur.depth+1,curLevel);
            }

            if(cur.node.right != null){
                queue.add(new TreeNodeAndDepth(cur.node.right,cur.depth+1));
                List<Integer> curLevel;
                if(map.containsKey(cur.depth+1)){
                    curLevel = map.get(cur.depth + 1);
                }
                else{
                    curLevel = new ArrayList<>();
                }
                curLevel.add(cur.node.right.val);
                map.put(cur.depth+1,curLevel);
            }

        }

    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        breathFirstSearch(root);
        result.addAll(map.values());
        return result;
    }
}