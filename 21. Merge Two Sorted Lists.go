package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func printLinkedList(head *ListNode) {
	cur := head

	for cur != nil {
		fmt.Println(cur.Val)
		cur = cur.Next
	}
}

var result *ListNode

func addToResult(val int) {
	cur := result
	for cur.Next != nil {
		cur = cur.Next
	}
	cur.Next = &ListNode{val, nil}
}

func recursiveTraversal(head1, head2 *ListNode) {
	if head1 == nil && head2 == nil {
		return
	} else if head1 == nil {
		addToResult(head2.Val)
		recursiveTraversal(head1, head2.Next)
	} else if head2 == nil {
		addToResult(head1.Val)
		recursiveTraversal(head1.Next, head2)
	} else {
		if head1.Val > head2.Val {
			addToResult(head2.Val)
			recursiveTraversal(head1, head2.Next)
		} else {
			addToResult(head1.Val)
			recursiveTraversal(head1.Next, head2)
		}
	}
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	if list1 == nil && list2 == nil {
		return list1
	} else if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	result = &ListNode{}
	cur1 := list1
	cur2 := list2
	recursiveTraversal(cur1, cur2)

	for result != nil && result.Val == 0 {
		result = result.Next
	}

	return result
}

func main() {

	head1 := &ListNode{1, nil}
	l2 := &ListNode{2, nil}
	l3 := &ListNode{4, nil}

	head2 := &ListNode{1, nil}
	l4 := &ListNode{3, nil}
	l5 := &ListNode{4, nil}

	head1.Next = l2
	l2.Next = l3

	head2.Next = l4
	l4.Next = l5

	answer := mergeTwoLists(head1, head2)
	printLinkedList(answer)

}
