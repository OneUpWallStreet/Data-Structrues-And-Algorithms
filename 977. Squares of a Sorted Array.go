package main

import (
	"fmt"
	"math"
)

func swap(nums []int, i, j int) {
	temp := nums[i]
	nums[i] = nums[j]
	nums[j] = temp
}

func sortedSquares(nums []int) []int {
	result := make([]int, len(nums))
	i := 0
	j := len(nums) - 1

	for k := len(nums) - 1; k >= 0; k-- {

		if math.Abs(float64(nums[i])) > math.Abs(float64(nums[j])) {
			result[k] = nums[i] * nums[i]
			i++
		} else {
			result[k] = nums[j] * nums[j]
			j--
		}
	}
	return result
}

func main() {
	ans := sortedSquares([]int{-4, -1, 0, 3, 10})
	fmt.Println(ans)
}
