package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// [1,2,3,4,5,6,null,8]

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func depthFirstTraversal(node *TreeNode, depth int) int {
	if node == nil {
		return depth
	}
	depth++
	return max(depthFirstTraversal(node.Left, depth), depthFirstTraversal(node.Right, depth))
}

func checkTreeBalance(node *TreeNode, depth int, maxDepth int) bool {

	if node == nil {
		return (depth == maxDepth || depth == maxDepth-1)
	}
	depth++
	if node.Left == nil && node.Right == nil {
		return (depth == maxDepth || depth == maxDepth-1)
	}
	return (checkTreeBalance(node.Left, depth, maxDepth) && checkTreeBalance(node.Right, depth, maxDepth))

}

func isBalanced(root *TreeNode) bool {
	maxDepth := depthFirstTraversal(root, 0)
	return checkTreeBalance(root, 0, maxDepth)
}

func main() {

	root := &TreeNode{1, nil, nil}
	n2 := &TreeNode{2, nil, &TreeNode{3, nil, nil}}
	root.Right = n2

	// r1 := &TreeNode{9, nil, nil}
	// root := &TreeNode{3, nil, nil}

	// root.Left = r1

	// n2 := &TreeNode{20, nil, nil}

	// n3 := &TreeNode{15, nil, nil}
	// n4 := &TreeNode{7, nil, nil}

	// n2.Left = n3
	// n2.Right = n4

	// root.Right = n2

	answer := isBalanced(root)

	fmt.Println("Answer is: ", answer)

}
