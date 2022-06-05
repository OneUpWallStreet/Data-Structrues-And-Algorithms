package main

import (
	"fmt"
	"sort"
)

func partitionArray(nums []int, k int) int {

	sort.Ints(nums)

	dif := nums[0] + k

	resultArr := [][]int{}
	currentArr := []int{}

	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		if nums[i] <= dif {
			currentArr = append(currentArr, nums[i])
		} else {
			resultArr = append(resultArr, currentArr)
			currentArr = []int{}
			dif = k + nums[i]
			currentArr = append(currentArr, nums[i])
		}
	}

	if len(currentArr) > 0 {
		resultArr = append(resultArr, currentArr)
	}

	return len(resultArr)
}

func main() {

	partitionArray([]int{2, 2, 4, 5}, 0)
	fmt.Println("Hello World")
}
