package main

import "fmt"

func trueOrFalse(v1, v2 bool) bool {
	return v1 == true || v2 == true
}

func recursiveJumping(nums []int, index int) bool {
	if index >= len(nums) {
		return false
	} else if index == len(nums)-1 {
		return true
	} else {
		jumpTarget := nums[index]
		answer := false
		for i := 1; i <= jumpTarget; i++ {
			answer = trueOrFalse(answer, recursiveJumping(nums, index+i))
		}
		return answer
	}
}

func canJump(nums []int) bool {
	return recursiveJumping(nums, 0)
}

func main() {
	nums := []int{3, 2, 1, 0, 4}
	answer := canJump(nums)
	fmt.Println("Answer: ", answer)
}
