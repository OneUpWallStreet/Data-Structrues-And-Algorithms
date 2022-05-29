package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func depthFirstTraversal(node *TreeNode, target int, set map[int]bool) bool {
	if node == nil {
		return false
	} else if set[target-node.Val] == true && node.Val != target-node.Val {
		return true
	}
	return depthFirstTraversal(node.Left, target, set) || depthFirstTraversal(node.Right, target, set)
}

func initSet(node *TreeNode, set *map[int]bool) {
	if node == nil {
		return
	}
	(*set)[node.Val] = true
	initSet(node.Left, set)
	initSet(node.Right, set)
}

func findTarget(root *TreeNode, k int) bool {

	if root.Left == nil && root.Right == nil {
		return false
	}

	set := map[int]bool{}
	initSet(root, &set)
	return depthFirstTraversal(root, k, set)

}

func main() {

	root := &TreeNode{2, nil, &TreeNode{3, nil, nil}}

	answer := findTarget(root, 6)
	fmt.Println("Answer: ", answer)

}
