package main

import (
	"fmt"
	"math"
)

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

func findDisappearedNumbers(nums []int) []int {

	// Create set from current array in place
	for i := 0; i < len(nums); i++ {
		val := abs(nums[i])
		if nums[val-1] < 0 {
			continue
		}
		nums[val-1] = -nums[val-1]
	}

	result := []int{}

	// Missing numbers are positive
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			result = append(result, i+1)
		}
	}

	return result
}

func main() {
	ans := findDisappearedNumbers([]int{4, 3, 2, 7, 8, 2, 3, 1})
	fmt.Println(ans)
}
