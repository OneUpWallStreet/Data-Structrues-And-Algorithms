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

func dynamicProgrammingSolution(index, loot int, nums []int, cache map[int]int) int {

	loot += nums[index]

	// fmt.Println(loot)

	if _, didFind := cache[index]; didFind {
		// fmt.Printf("cache Val: %v and loot val: %v  and index: %v \n", cache[index], loot, index)
		return cache[index]
	}

	// if index == len(nums)-1 {
	// 	cache[index] = loot
	// 	return loot
	// }

	maxVal := loot
	for i := index + 2; i < len(nums); i++ {
		maxVal = max(maxVal, dynamicProgrammingSolution(i, loot, nums, cache))
	}

	cache[index] = maxVal
	return maxVal
}

func printCache(cache map[int]int) {
	fmt.Println()

	for key, val := range cache {
		fmt.Printf("key: %v and Val: %v \n", key, val)
	}
	fmt.Println()

}

func rob(nums []int) int {
	var loot int
	cache := map[int]int{}
	for i := len(nums) - 1; i >= 0; i-- {
		// fmt.Println("\n root index: ", i)
		loot = max(loot, dynamicProgrammingSolution(i, 0, nums, cache))
		printCache(cache)
	}

	return loot
}

func main() {
	ans := rob([]int{1, 2, 3, 1})
	fmt.Println("answer is: ", ans)
}
