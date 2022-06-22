package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func convertLinkedListToSlice(head *ListNode) []int {
	cur := head
	result := []int{}
	for cur != nil {
		result = append(result, cur.Val)
		cur = cur.Next
	}
	return result
}

func findTwinOfIndex(i, n int) int {
	return (n - 1) - i
}

func pairSum(head *ListNode) int {
	array := convertLinkedListToSlice(head)
	answer := -1
	for i := 0; i <= (len(array)/2 - 1); i++ {
		fmt.Println(i)
		answer = max(answer, array[i]+array[findTwinOfIndex(i, len(array))])
	}
	return answer
}

func main() {

	head := &ListNode{5, nil}
	l2 := &ListNode{4, nil}
	l3 := &ListNode{2, nil}
	l4 := &ListNode{1, nil}

	head.Next = l2
	l2.Next = l3
	l3.Next = l4

	answer := pairSum(head)

	fmt.Println("Answer: ", answer)

}
