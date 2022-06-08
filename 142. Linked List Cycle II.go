package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	set := map[*ListNode]bool{}
	cur := head
	for cur != nil {
		if _, didFind := set[cur]; didFind {
			return cur
		}
		set[cur] = true
		cur = cur.Next
	}
	return nil
}
