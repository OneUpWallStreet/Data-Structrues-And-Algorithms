package main

func fetchNextIndex(index, k, len int) int {
	if index+k < len {
		return index + k
	}
	return fetchNextIndex(0, (index+k)-len, len)
}

func rotate(nums []int, k int) {
	k = k % len(nums)
	result := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		newIndex := fetchNextIndex(i, k, len(nums))
		result[newIndex] = nums[i]
	}
	nums = result
}

func main() {
	rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3)
}
