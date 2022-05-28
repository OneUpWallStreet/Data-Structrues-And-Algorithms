package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestorRecursive(root, p, q *TreeNode) *TreeNode {

	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestorRecursive(root.Left, p, q)
	} else if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestorRecursive(root.Right, p, q)
	} else {
		return root
	}

}

func lowestCommonAncestorIterative(root, p, q *TreeNode) *TreeNode {
	cur := root
	for true {
		if p.Val < cur.Val && q.Val < cur.Val {
			cur = cur.Left
		} else if p.Val > cur.Val && q.Val > cur.Val {
			cur = cur.Right
		} else {
			break
		}
	}
	return cur
}

func main() {
	fmt.Println("Hello World")
}
