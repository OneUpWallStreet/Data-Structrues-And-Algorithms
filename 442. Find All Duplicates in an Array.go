package main

import (
	"fmt"
	"math"
)

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

func findDuplicates(nums []int) []int {

	result := []int{}

	for i := 0; i < len(nums); i++ {

		val := abs(nums[i])

		if nums[val-1] < 0 {
			result = append(result, val)
			continue
		}

		nums[val-1] = -nums[val-1]
	}

	return result
}

func main() {

	ans := findDuplicates([]int{10, 2, 5, 10, 9, 1, 1, 4, 3, 7})
	fmt.Println("Answer: ", ans)
}
