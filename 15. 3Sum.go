package main

import (
	"fmt"
	"sort"
)

type ValPair struct {
	v1 int
	v2 int
}

func twoSum(nums []int, result [][]int, start, end, target int, resultSet map[[3]int]bool) [][]int {

	i := start
	j := end

	for i < j {
		if nums[i]+nums[j] == target {

			valArray := [3]int{-target, nums[i], nums[j]}
			sort.Ints(valArray[:])
			if _, didFind := resultSet[valArray]; !didFind {
				result = append(result, []int{valArray[0], valArray[1], valArray[2]})
				resultSet[valArray] = true
			}
			i++
			for nums[i] == nums[i-1] && i < j {
				i++
			}
		} else if nums[i]+nums[j] < target {
			i++
		} else if nums[i]+nums[j] > target {
			j--
		}
	}
	return result

}

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}

	resultSet := map[[3]int]bool{}

	for i := 0; i < len(nums); i++ {
		result = twoSum(nums, result, i+1, len(nums)-1, -nums[i], resultSet)
	}

	return result
}

func main() {

	input := []int{-1, 0, 1, 2, -1, -4}
	answer := threeSum(input)
	fmt.Println(answer)
}
