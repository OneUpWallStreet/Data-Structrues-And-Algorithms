package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func minimalKSum(nums []int, k int) int64 {

	set := map[int]bool{}
	for i := 0; i < len(nums); i++ {
		set[nums[i]] = true
	}

	var i int = 1
	sum := 0

	for k > 0 {
		if _, didFind := set[i]; !didFind {
			sum += i
			k--
		}
		i++
	}

	return int64(sum)

}

func main() {
	ans := minimalKSum([]int{5, 6}, 6)
	fmt.Println("answer: ", ans)
}
