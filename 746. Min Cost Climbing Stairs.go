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

func recursiveClimbing(cost []int, index int) int {
	if index < 0 {
		return 0
	} else if didHitCostCache(costCache, index) {
		return costCache[index]
	} else if index <= 0 || index == 1 {
		return cost[index]
	}
	costCache[index] = cost[index] + min(recursiveClimbing(cost, index-1), recursiveClimbing(cost, index-2))
	return costCache[index]
}

func minCostClimbingStairs(cost []int) int {
	costCache = map[int]int{}
	return min(recursiveClimbing(cost, len(cost)-1), recursiveClimbing(cost, len(cost)-2))
}

func main() {
	cost := []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
	answer := minCostClimbingStairs(cost)
	fmt.Println("Answer: ", answer)
}
