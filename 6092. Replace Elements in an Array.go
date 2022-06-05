package main

import "fmt"

func arrayChange(nums []int, operations [][]int) []int {

	indexMap := map[int]int{}

	for i := 0; i < len(nums); i++ {
		indexMap[nums[i]] = i
	}

	for i := 0; i < len(operations); i++ {
		indexOfNumber := indexMap[operations[i][0]]
		nums[indexOfNumber] = operations[i][1]
		indexMap[operations[i][0]] = -1
		indexMap[operations[i][1]] = indexOfNumber
	}

	return nums
}

func main() {
	fmt.Println(arrayChange([]int{1, 2, 4, 6}, [][]int{{1, 3}, {4, 7}, {6, 1}}))
}
