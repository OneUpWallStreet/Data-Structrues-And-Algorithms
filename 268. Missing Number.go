package main

import (
	"fmt"
	"sort"
)

// Time - O(n)
// Space - O(n)

func missingNumber(nums []int) int {
	n := len(nums)
	set := map[int]bool{}
	for i := 0; i < n; i++ {
		set[nums[i]] = true
	}
	for i := 0; i < n; i++ {
		if set[i] == false {
			return i
		}
	}
	return n
}

// Time - O(nlogn)
// Space - O(1)

func missingNumber2(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	checker := 0
	for i := 0; i < n; i++ {
		if nums[i] != checker {
			return i
		}
		checker++
	}
	return n
}

func main() {
	nums := []int{9, 6, 4, 2, 3, 5, 7, 0, 1}
	answer := missingNumber(nums)
	fmt.Println("Answer: ", answer)
}
