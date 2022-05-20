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
    
    func depthFirstTraversal(node: TreeNode?, leftBoundry: Int, rightBoundry: Int) -> Bool{
        
        if(node == nil){
            return true
        }
        
        
        if(!(node!.val > leftBoundry && node!.val < rightBoundry)){
            return false
        }
        
        
        return (depthFirstTraversal(node: node?.left, leftBoundry: leftBoundry, rightBoundry: node!.val) && depthFirstTraversal(node: node?.right, leftBoundry: node!.val, rightBoundry: rightBoundry))
        
    }
    
    func isValidBST(_ root: TreeNode?) -> Bool {
        return depthFirstTraversal(node: root, leftBoundry: Int.min, rightBoundry: Int.max)
    }
}
