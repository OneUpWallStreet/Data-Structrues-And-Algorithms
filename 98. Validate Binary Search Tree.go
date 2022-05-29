package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func depthFirstTraversal(root *TreeNode, min, max int) bool {

	if root == nil || (root.Left == nil && root.Right == nil) {
		return true
	} else if root.Left == nil {
		return (root.Right.Val > root.Val && root.Right.Val > min && root.Right.Val < max)
	} else if root.Right == nil {
		return root.Left.Val < root.Val && root.Left.Val < min
	} else if root.Left.Val >= root.Val || root.Right.Val <= root.Val || root.Left.Val > min || root.Right.Val < max {
		fmt.Println("Killed here")
		fmt.Println("Root val: ", root.Val)
		fmt.Println("Left val: ", root.Left.Val)
		fmt.Println("Right val: ", root.Right.Val)
		fmt.Printf("min: %v & max: %v \n", min, max)
		return false
	}

	return depthFirstTraversal(root.Left, root.Left.Val, max) && depthFirstTraversal(root.Right, min, root.Right.Val)

}

func isValidBST(root *TreeNode) bool {
	return depthFirstTraversal(root, root.Left.Val, root.Right.Val)
}

func main() {

	node := &TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}

	ans := isValidBST(node)

	fmt.Println("Answer is: ", ans)

	// fmt.Println("Beast")
}
