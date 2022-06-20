package main

func pivotIndex(nums []int) int {

	leftMap := map[int]int{}
	rightMap := map[int]int{}

	curSum := 0

	for i := 0; i < len(nums); i++ {
		curSum += nums[i]
		leftMap[i] = curSum
	}

	curSum = 0

	for i := len(nums) - 1; i >= 0; i-- {
		curSum += nums[i]
		rightMap[i] = curSum
	}

	for i := 0; i < len(nums); i++ {
		if leftMap[i] == rightMap[i] {
			return i
		}
	}

	return -1
}

func main() {

}
