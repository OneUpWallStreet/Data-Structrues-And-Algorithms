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

func reverseLinkedList(head *ListNode) *ListNode {
	cur := head
	var prev *ListNode = nil
	var next *ListNode = nil
	for cur != nil {
		next = cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
}

func linkedListToSlice(head *ListNode) []int {
	result := []int{}
	cur := head
	for cur != nil {
		result = append(result, cur.Val)
		cur = cur.Next
	}
	return result
}

func isPalindrome(head *ListNode) bool {

	orginalLinkedList := linkedListToSlice(head)
	reversedLinkedList := linkedListToSlice(reverseLinkedList(head))

	i := 0

	for i < len(orginalLinkedList) {
		if orginalLinkedList[i] != reversedLinkedList[i] {
			return false
		}
		i++
	}

	return true
}

func main() {

	head := &ListNode{1, nil}
	l2 := &ListNode{2, nil}

	head.Next = l2

	answer := isPalindrome(head)

	fmt.Println("Answer: ", answer)

}
