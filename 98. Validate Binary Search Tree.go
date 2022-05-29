package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {

	if root == nil || (root.Left == nil && root.Right == nil) {
		return true
	} else if root.Left == nil || root.Right == nil {
		return false
	} else if root.Left.Val >= root.Val || root.Right.Val <= root.Val {
		return false
	}

	return isValidBST(root.Left) && isValidBST(root.Right)
}

func main() {
	fmt.Println("Beast")
}
