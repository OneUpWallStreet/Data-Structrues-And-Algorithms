package main

import (
	"fmt"
)

func bruteForceSolution(index int, nums []int) int {

	loot := 0

	for index < len(nums) {
		loot += nums[index]
		index += 2
	}

	return loot
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func rob(nums []int) int {
	loot := 0
	for i := 0; i < len(nums); i++ {
		loot = max(loot, bruteForceSolution(i, nums))
	}
	return loot
}

func main() {
	ans := rob([]int{2, 7, 9, 3, 1})
	fmt.Println("answer is: ", ans)
}
