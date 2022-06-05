package main

import (
	"fmt"
	"math"
)

func majorityElement(nums []int) []int {

	condition := int(math.Floor(float64(len(nums) / 3)))
	result := []int{}
	freqMap := map[int]int{}

	for i := 0; i < len(nums); i++ {
		if _, didFind := freqMap[nums[i]]; didFind {
			freqMap[nums[i]]++
		} else {
			freqMap[nums[i]] = 1
		}
	}

	for num, freq := range freqMap {
		if freq > condition {
			result = append(result, num)
		}
	}

	return result

}

func main() {
	fmt.Println(majorityElement([]int{3, 2, 3}))
}
