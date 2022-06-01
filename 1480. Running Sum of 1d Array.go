package main

import (
	"fmt"
)

func runningSum(nums []int) []int {
	sum := nums[0]
	result := []int{nums[0]}
	for i := 1; i < len(nums); i++ {
		sum += nums[i]
		result = append(result, sum)
	}
	return result
}

func main() {

	input := []int{1, 2, 3, 4}
	answer := runningSum(input)

	fmt.Println("Answer is: ", answer)
}
