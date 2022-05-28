package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {

	if head == nil || head.Next == nil {
		return false
	}

	slow := head
	fast := head.Next

	for fast != nil && fast.Next != nil {
		if fast == slow {
			return true
		}
		slow = slow.Next
		fast = fast.Next.Next
	}

	return false
}

func main() {

	l1 := &ListNode{3, nil}
	l2 := &ListNode{2, nil}
	l3 := &ListNode{0, nil}
	l4 := &ListNode{-4, nil}

	l1.Next = l2
	l2.Next = l3
	l3.Next = l4
	l4.Next = l2

	answer := hasCycle(l1)

	fmt.Println("ANswer: ", answer)
}
