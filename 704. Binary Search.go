package main

import "fmt"

func binarySearch(nums []int, target, left, right int) int {
	if left <= right {
		mid := left + (right-left)/2

		if nums[mid] == target {
			return mid
		}
		if nums[mid] < target {
			return binarySearch(nums, target, mid+1, right)
		} else {
			return binarySearch(nums, target, left, mid-1)
		}
	}
	return -1
}

func search(nums []int, target int) int {
	return binarySearch(nums, target, 0, len(nums)-1)
}

func main() {
	// [-1,0,3,5,9,12]
	// 9

	answer := search([]int{-1, 0, 3, 5, 9, 12}, 9)

	fmt.Println("Answer: ", answer)
}
