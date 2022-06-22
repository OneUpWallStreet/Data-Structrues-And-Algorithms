package main

import "fmt"

func canJump(nums []int) bool {
	goal := len(nums) - 1
	for i := len(nums) - 1; i >= 0; i++ {
		if i+nums[i] >= goal {
			goal = i
		}
	}
	return goal == 0
}

func main() {
	nums := []int{2, 3, 1, 1, 4}
	answer := canJump(nums)
	fmt.Println("Answer: ", answer)
}
