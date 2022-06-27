//  Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
      self.val = val
      self.left = left
      self.right = right
  }
}

 
class Solution {
    
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        // Should never execute
        guard let root = root else {
            return nil
        }
        if p!.val > root.val && q!.val > root.val {
            return lowestCommonAncestor(root.right, p, q)
        }else if p!.val < root.val && q!.val < root.val {
            return lowestCommonAncestor(root.left, p, q)
        }else{
            return root
        }
    }
    
}