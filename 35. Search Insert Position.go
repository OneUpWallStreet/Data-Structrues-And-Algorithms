package main

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
	return left
}

func searchInsert(nums []int, target int) int {
	return binarySearch(nums, target, 0, len(nums)-1)
}
