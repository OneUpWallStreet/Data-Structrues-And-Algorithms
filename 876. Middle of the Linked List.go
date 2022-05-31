package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getMiddleIndex(node *ListNode) int {
	counter := 0
	for node != nil {
		counter++
		node = node.Next
	}
	return (counter / 2) - 1
}

func middleNode(head *ListNode) *ListNode {
	mid := getMiddleIndex(head)
	index := 0
	cur := head
	for index <= mid {
		cur = cur.Next
		index++
	}
	return cur
}

func main() {
}
