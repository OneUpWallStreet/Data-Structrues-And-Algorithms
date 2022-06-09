package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func firstMissingPositive(nums []int) int {

	freqMap := map[int]bool{}

	var maxNum int

	for i := 0; i < len(nums); i++ {
		maxNum = max(maxNum, nums[i])
		freqMap[nums[i]] = true
	}

	for i := 1; i <= maxNum+1; i++ {
		if _, didFind := freqMap[nums[i]]; !didFind {
			return i
		}
	}

	return -1

}

func main() {
	ans := firstMissingPositive([]int{3, 4, -1, 1})
	fmt.Println(ans)
}
