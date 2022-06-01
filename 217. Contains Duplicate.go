package main

import (
	"fmt"
)

func containsDuplicate(nums []int) bool {
	set := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		if _, didFind := set[nums[i]]; didFind {
			return true
		} else {
			set[nums[i]] = true
		}
	}
	return false
}

func main() {

	input := []int{1, 2, 3, 1}

	fmt.Println(input)

}
