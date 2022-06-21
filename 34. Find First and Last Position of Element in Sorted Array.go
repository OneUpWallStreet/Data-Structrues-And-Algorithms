package main

import "fmt"

func binarySearch(nums []int, first bool, target int) int {
	left := 0
	right := len(nums) - 1
	result := -1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			result = mid
			if first {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if target < nums[mid] {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return result

}

func searchRange(nums []int, target int) []int {
	first := binarySearch(nums, true, target)
	last := binarySearch(nums, false, target)
	return []int{first, last}
}

func main() {
	ans := searchRange([]int{5, 7, 7, 8, 8, 10}, 8)
	fmt.Println("answer: ", ans)
}
