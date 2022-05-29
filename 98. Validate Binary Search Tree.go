package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func depthFirstTraversal(root *TreeNode, min, max int) bool {

	if root == nil {
		return true
	} else if root.Val <= min || root.Val >= max {
		return false
	} else if root.Left == nil && root.Right == nil {
		return true
	}

	return depthFirstTraversal(root.Left, min, root.Val) && depthFirstTraversal(root.Right, root.Val, max)

}

func isValidBST(root *TreeNode) bool {
	return depthFirstTraversal(root, -math.MaxInt64, math.MaxInt64)
}

func main() {
	node := &TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}
	ans := isValidBST(node)
	fmt.Println("Answer is: ", ans)
}
