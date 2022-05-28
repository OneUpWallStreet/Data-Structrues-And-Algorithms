package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {

	if root == nil || root.Val == val {
		return root
	}

	var node *TreeNode = searchBST(root.Left, val)

	if node == nil {
		node = searchBST(root.Right, val)
	}

	return node
}

func main() {
}
