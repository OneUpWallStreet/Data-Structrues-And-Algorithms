package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

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

func checkValue(x, y int) bool {
	return x == y || max(x, y)-min(x, y) == 1
}

func isBalanced(root *TreeNode) bool {

	if root == nil {
		return true
	}

	var leftHeight int = depthFirstTraversal(root.Left, 0)
	var rightHeight int = depthFirstTraversal(root.Right, 0)

	return checkValue(leftHeight, rightHeight) && isBalanced(root.Left) && isBalanced(root.Right)

}

func main() {

	root := &TreeNode{1, nil, nil}
	n2 := &TreeNode{2, nil, &TreeNode{3, nil, nil}}
	root.Right = n2

	answer := isBalanced(root)

	fmt.Println("Answer is: ", answer)

}
