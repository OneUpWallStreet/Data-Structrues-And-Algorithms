package main

import (
	"fmt"
	"sort"
)

type ValPair struct {
	v1 int
	v2 int
}

func twoSum(nums []int, start, end, target int) (bool, ValPair) {

	i := start
	j := end

	for i < j {
		if nums[i]+nums[j] == target {
			return true, ValPair{nums[i], nums[j]}
		} else if nums[i]+nums[j] < target {
			i++
		} else if nums[i]+nums[j] > target {
			j--
		}
	}
	return false, ValPair{-1, -1}

}

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}

	resultSet := map[[3]int]bool{}

	for i := 0; i < len(nums); i++ {
		didFind, valPair := twoSum(nums, i+1, len(nums)-1, -nums[i])
		if didFind {
			valArray := [3]int{nums[i], valPair.v1, valPair.v2}
			sort.Ints(valArray[:])
			if _, didFind := resultSet[valArray]; didFind {
				continue
			} else {
				result = append(result, []int{nums[i], valPair.v1, valPair.v2})
				resultSet[valArray] = true
			}
		}
	}

	return result
}

func main() {

	input := []int{-1, 0, 1, 2, -1, -4}
	answer := threeSum(input)
	fmt.Println(answer)
}
