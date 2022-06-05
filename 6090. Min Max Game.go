package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {

	if x > y {
		return x
	}

	return y
}

func minMaxGame(nums []int) int {

	if len(nums) == 1 {
		return nums[0]
	}

	newNums := []int{}

	for i := 0; i < len(nums)/2; i++ {
		if (i % 2) == 0 {
			newNums = append(newNums, min(nums[i*2], nums[i*2+1]))
		} else {
			newNums = append(newNums, max(nums[i*2], nums[i*2+1]))
		}
	}

	return minMaxGame(newNums)
}

func main() {
	fmt.Println("Hello World")

}
