package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

var costCache map[int]int

func didHitCostCache(cache map[int]int, index int) bool {
	_, didFind := cache[index]
	return didFind
}

func recursiveClimbing(cost []int, index, costSum int) int {

	if didHitCostCache(costCache, index) {
		return costCache[index]
	} else if index >= len(cost) {
		return costSum
	}

	costSum += cost[index]
	costCache[index] = min(recursiveClimbing(cost, index+1, costSum), recursiveClimbing(cost, index+2, costSum))
	return costCache[index]

}

func minCostClimbingStairs(cost []int) int {
	costCache = map[int]int{}
	return min(recursiveClimbing(cost, 0, 0), recursiveClimbing(cost, 1, 0))
}

func main() {

	cost := []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
	answer := minCostClimbingStairs(cost)

	fmt.Println("Answer: ", answer)

}
