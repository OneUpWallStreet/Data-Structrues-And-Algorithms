package main

import (
	"fmt"
	"math"
)

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

func firstMissingPositive(nums []int) int {

	// Replace all the negative numbers with 0
	for i := 0; i < len(nums); i++ {
		if nums[i] < 0 {
			nums[i] = 0
		}
	}

	// Traverse array again and mark elements
	for i := 0; i < len(nums); i++ {

		// Check for out of bounds
		if abs(nums[i])-1 < 0 || abs(nums[i])-1 >= len(nums) {
			continue
		}

		// We have alraedy marked the element
		if nums[abs(nums[i])-1] < 0 {
			continue
		}

		if nums[abs(nums[i])-1] == 0 {
			nums[abs(nums[i])-1] = -(len(nums) + 1)
		} else {
			nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
		}

	}

	for i := 1; i <= len(nums); i++ {
		if nums[i-1] >= 0 {
			return i
		}
	}

	return len(nums) + 1

}

func main() {
	ans := firstMissingPositive([]int{0})
	fmt.Println(ans)
}
