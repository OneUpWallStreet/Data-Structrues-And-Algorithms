package main

import (
	"fmt"
)

var minOperationsCount int = -1

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func storeResult(operationCount int) {
	if minOperationsCount == -1 {
		minOperationsCount = operationCount
	} else {
		minOperationsCount = min(minOperationsCount, operationCount)
	}
}

func recursiveOperations(nums []int, xLeft, i, j, operationCount int) {

	if xLeft == 0 {
		storeResult(operationCount)
		return
	} else if xLeft < 0 {
		return
	}

	operationCount++

	if i <= j {
		// Pop Left
		recursiveOperations(nums, xLeft-nums[i], i+1, j, operationCount)

		// Pop Right
		recursiveOperations(nums, xLeft-nums[j], i, j-1, operationCount)
	}

}

func minOperations(nums []int, x int) int {
	minOperationsCount = -1
	recursiveOperations(nums, x, 0, len(nums)-1, 0)
	return minOperationsCount
}

func main() {

	input := []int{8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309}
	x := 134365

	answer := minOperations(input, x)
	fmt.Println(answer)

}
