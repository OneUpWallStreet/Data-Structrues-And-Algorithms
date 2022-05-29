package main

import "fmt"

func majorityElement(nums []int) int {

	freqMap := map[int]int{}

	for i := 0; i < len(nums); i++ {
		if _, didFind := freqMap[nums[i]]; didFind {
			freqMap[nums[i]]++
		} else {
			freqMap[nums[i]] = 1
		}
	}

	for num, freq := range freqMap {
		if (freq) > len(nums)/2 {
			return num
		}
	}

	return -1
}

func main() {
	fmt.Println("Hey")
}
