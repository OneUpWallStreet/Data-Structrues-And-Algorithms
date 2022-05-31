package main

import (
	"fmt"
)

var totalSteps int = 0
var cache map[int]int

func recursiveSoln(n int) {

	if _, didFind := cache[n]; didFind {
		totalSteps += cache[n]
		return
	} else if n == 0 {
		totalSteps++
		return
	}

	if n-1 >= 0 {
		recursiveSoln(n - 1)
	}
	if n-2 >= 0 {
		recursiveSoln(n - 2)
	}

}

func climbStairs(n int) int {
	cache = map[int]int{}

	for i := 1; i <= n; i++ {
		totalSteps = 0
		recursiveSoln(i)
		cache[i] = totalSteps
	}

	return totalSteps
}

func main() {

	fmt.Println("Answer: ", climbStairs(44))

}
