package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func depthFirstSearch(node *TreeNode, depth int) int {
	if node == nil {
		return depth
	}
	depth++
	return max(depthFirstSearch(node.Left, depth), depthFirstSearch(node.Right, depth))

}

func maxDepth(root *TreeNode) int {
	return depthFirstSearch(root, 0)
}

func main() {

}
