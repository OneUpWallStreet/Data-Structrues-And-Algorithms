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

func dynamicProgrammingSolution(index int, nums []int, cache map[int]int) int {
	if index >= len(nums) {
		return 0
	}

	if _, didFind := cache[index]; didFind {
		return cache[index]
	}

	cache[index] = max(dynamicProgrammingSolution(index+1, nums, cache), nums[index]+dynamicProgrammingSolution(index+2, nums, cache))
	return cache[index]
}

func rob(nums []int) int {
	return dynamicProgrammingSolution(0, nums, map[int]int{})
}

func main() {
	ans := rob([]int{1, 2, 1, 1})
	fmt.Println("answer is: ", ans)
}
