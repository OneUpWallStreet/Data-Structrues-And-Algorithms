package main

import (
	"fmt"
)

var totalSteps int = 0
var cache map[int]int

func recursiveSoln(n int) {
	if n == 0 {
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
	totalSteps = 0
	cache = map[int]int{}
	recursiveSoln(n)
	return totalSteps
}

func main() {

	fmt.Println("Answer: ", climbStairs(44))

}
