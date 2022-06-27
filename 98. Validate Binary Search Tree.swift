import Foundation

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
    
    private func recursiveValidation(node: TreeNode?,max: Int, min: Int) -> Bool {

        // If node is nil, than of-course it's valid
        guard let node = node else {
            return true
        }
       
       // Check if current node is valid
        if node.val >= max || node.val <= min {
            return false
        }
        
        // Both children are nil
        if node.left == nil && node.right == nil {
            return true
        }
        
        // Only left subtree is exists
        else if node.left != nil && node.right == nil{
            return recursiveValidation(node: node.left, max: node.val, min: min)
        }
        
        // Only Right subtree is exists
        else if node.right != nil && node.left == nil {
            return recursiveValidation(node: node.right, max: max, min: node.val)
        }

        // Both children exist! Yay
        return recursiveValidation(node: node.left, max: node.val, min: min) && recursiveValidation(node: node.right, max: max, min: node.val)
        
    }
    
   func isValidBST(_ root: TreeNode?) -> Bool {
       return recursiveValidation(node: root, max: Int.max, min: Int.min)
   }
}