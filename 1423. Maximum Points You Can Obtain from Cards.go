package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

type cacheCell struct {
	left, right, k int
}

var cache map[cacheCell]int

func didHitCache(cache map[cacheCell]int, cell cacheCell) bool {
	_, didFind := cache[cell]
	return didFind
}

func recursiveTraversal(cardPoints []int, k, left, right, score int) int {
	if k == 0 {
		return score
	} else if didHitCache(cache, cacheCell{left, right, k}) {
		return cache[cacheCell{left, right, k}]
	}
	leftScore := recursiveTraversal(cardPoints, k-1, left+1, right, score+cardPoints[left])
	rightScore := recursiveTraversal(cardPoints, k-1, left, right-1, score+cardPoints[right])
	cache[cacheCell{left, right, k}] = max(leftScore, rightScore)
	return cache[cacheCell{left, right, k}]
}

func maxScore(cardPoints []int, k int) int {
	cache = map[cacheCell]int{}
	return recursiveTraversal(cardPoints, k, 0, len(cardPoints)-1, 0)
}

func main() {
	answer := maxScore([]int{53, 14, 91, 35, 51, 9, 80, 27, 6, 15, 77, 86, 34, 62, 55, 45, 91, 45, 23, 75, 66, 42, 62, 13, 34, 18, 89, 67, 93, 83, 100, 14, 92, 73, 48, 2, 47, 93, 99, 100, 88, 84, 48}, 43)
	fmt.Println("Answer: ", answer)
}
