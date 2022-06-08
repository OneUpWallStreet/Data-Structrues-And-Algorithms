package main

import (
	"fmt"
)

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

func fetchDuplicates(head *ListNode) map[int]bool {

	cur := head
	set := map[int]bool{}
	duplicateSet := map[int]bool{}

	for cur != nil {
		if _, didFind := set[cur.Val]; didFind {
			duplicateSet[cur.Val] = true
		} else {
			set[cur.Val] = true
		}
		cur = cur.Next
	}

	return duplicateSet

}

func deleteDuplicates(head *ListNode) *ListNode {
	set := fetchDuplicates(head)

	cur := head

	if cur == nil {
		return head
	}

	if set[head.Val] {
		for head != nil && set[head.Val] {
			head = head.Next
		}
	}

	for cur != nil {
		if cur.Next != nil && set[cur.Next.Val] {
			cur.Next = cur.Next.Next
		} else {
			cur = cur.Next
		}
	}
	printLinkedList(head)
	return head
}

func main() {

	l1 := &ListNode{1, nil}
	l2 := &ListNode{1, nil}
	l3 := &ListNode{3, nil}
	l4 := &ListNode{3, nil}
	l5 := &ListNode{4, nil}
	l6 := &ListNode{4, nil}
	l7 := &ListNode{5, nil}

	l1.Next = l2
	l2.Next = l3
	l3.Next = l4
	l4.Next = l5
	l5.Next = l6
	l6.Next = l7

	answer := deleteDuplicates(l1)

	fmt.Println(answer)

}
