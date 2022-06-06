package main

import (
	"fmt"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func bruteForceSolution(index, loot int, nums []int) int {

	loot += nums[index]

	if index == len(nums)-1 {
		return loot
	}

	maxVal := loot

	for i := index + 2; i < len(nums); i++ {
		maxVal = max(maxVal, bruteForceSolution(i, loot, nums))
	}

	return maxVal

}

func rob(nums []int) int {
	var loot int
	for i := 0; i < len(nums); i++ {
		loot = max(loot, bruteForceSolution(i, 0, nums))
	}
	return loot
}

func main() {
	ans := rob([]int{1, 2, 3, 1})
	fmt.Println("answer is: ", ans)
}
