var output []int

func recursiveTraversal(node *Node) {
	if node == nil {
		return
	}
	output = append(output, node.Val)
	for i := 0; i < len(node.Children); i++ {
		recursiveTraversal(node.Children[i])
	}
}

func preorder(root *Node) []int {
	output = []int{}
	recursiveTraversal(root)
	return output
}