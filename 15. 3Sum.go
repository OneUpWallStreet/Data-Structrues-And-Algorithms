package main

import (
	"fmt"
	"sort"
)

func addToResult(result [][]int, resultHash map[[3]int]bool, n1, n2, n3 int) [][]int {
	if _, didFind := resultHash[[3]int{n1, n2, n3}]; didFind {
		return result
	} else {
		newRes := []int{n1, n2, n3}
		result = append(result, newRes)
		resultHash[[3]int{n1, n2, n3}] = true
	}
	return result
}

func threeSum(nums []int) [][]int {

	sort.Ints(nums)
	resultHash := map[[3]int]bool{}

	freqMap := map[int]int{}

	// Loop through array and store all the values,
	// with their freq
	for i := 0; i < len(nums); i++ {
		if _, didFind := freqMap[nums[i]]; didFind {
			freqMap[nums[i]]++
		} else {
			freqMap[nums[i]] = 1
		}
	}

	i := 0
	j := len(nums) - 1

	result := [][]int{}

	for i < j {
		sum := nums[i] + nums[j]

		fmt.Printf("i : %v j: %v & sum: %v \n", nums[i], nums[j], sum)

		// if sum+nums[i]+nums[j] == 0 {
		if _, didFind := freqMap[sum]; didFind {
			if sum == nums[i] || sum == nums[j] {
				if freqMap[nums[i]] > 1 {
					newValues := [3]int{nums[i], nums[j], sum}
					sort.Ints(newValues[:])
					result = addToResult(result, resultHash, newValues[0], newValues[1], newValues[2])
				}
			} else {
				newValues := [3]int{nums[i], nums[j], sum}
				sort.Ints(newValues[:])
				result = addToResult(result, resultHash, newValues[0], newValues[1], newValues[2])
			}
		}
		// }

		if nums[i] < sum {
			i++
		} else {
			j--
		}

	}

	return result
}

func main() {
	input := []int{-1, 0, 1, 2, -1, -4}
	answer := threeSum(input)
	fmt.Println(answer)
}
