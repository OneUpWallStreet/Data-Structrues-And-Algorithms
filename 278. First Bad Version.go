package main

import (
	"fmt"
	"math"
)

func isBadVersion(version int) bool {
	if version >= 1 {
		return true
	} else {
		return false
	}
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func binarySearch(minValue, left, right int) int {
	if left <= right {
		mid := left + (right-left)/2
		if isBadVersion(mid) {
			minValue = min(mid, minValue)
			return binarySearch(minValue, left, mid-1)
		} else {
			return binarySearch(minValue, mid+1, right)
		}
	}
	return minValue
}

func firstBadVersion(n int) int {
	return binarySearch(math.MaxInt64, 1, n)
}

func main() {
	fmt.Println(firstBadVersion(3))
}
