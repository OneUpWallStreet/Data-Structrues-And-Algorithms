package main

import (
	"fmt"
)

func singleNumber(nums []int) int {

	freqMap := map[int]int{}

	for i := 0; i < len(nums); i++ {
		if _, didFind := freqMap[nums[i]]; didFind {
			freqMap[nums[i]]++
		} else {
			freqMap[nums[i]] = 1
		}
	}

	for num, freq := range freqMap {
		if freq == 1 {
			return num
		}
	}

	return -1
}

func main() {
	fmt.Println("Cache is cool")
}
