package main

import (
	"fmt"
	"math"
)

type cell struct {
	x, y int
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func didHitCache(cache map[cell]int, x, y int) bool {
	_, didFind := cache[cell{x, y}]
	return didFind
}

func fetchNextCells(row []int, index int) []int {
	nextCells := []int{}
	if index+1 >= len(row) {
		nextCells = append(nextCells, index)
	} else {
		nextCells = append(nextCells, index)
		nextCells = append(nextCells, index+1)
	}
	return nextCells

}

func recursiveTraversal(traingle [][]int, rowIndex, colIndex, curSum int, cache map[cell]int) int {

	curSum += traingle[rowIndex][colIndex]
	rowIndex++

	// if didHitCache(cache, rowIndex, colIndex) {
	// 	fmt.Printf("didHitcache: %v and %v", rowIndex, colIndex)
	// 	return cache[cell{rowIndex, colIndex}]
	// }

	if rowIndex >= len(traingle) && didHitCache(cache, rowIndex, colIndex) {
		if curSum < cache[cell{rowIndex, colIndex}] {
			cache[cell{rowIndex, colIndex}] = curSum
			return curSum
		} else {
			return cache[cell{rowIndex, colIndex}]
		}
	} else if rowIndex >= len(traingle) {
		return curSum
	} else if didHitCache(cache, rowIndex, colIndex) {
		return cache[cell{rowIndex, colIndex}]
	}

	nextCells := fetchNextCells(traingle[rowIndex], colIndex)

	var minRes int = math.MaxInt64

	for i := 0; i < len(nextCells); i++ {
		minRes = min(recursiveTraversal(traingle, rowIndex, nextCells[i], curSum, cache), minRes)
		fmt.Println(minRes)
		// A cache to store the minimum value for a given cell.
		fmt.Printf("Storing %v and %v ", rowIndex, nextCells[i])
		cache[cell{rowIndex, nextCells[i]}] = minRes
	}
	return minRes
}

func minimumTotal(triangle [][]int) int {
	cache := map[cell]int{}
	ans := recursiveTraversal(triangle, 0, 0, 0, cache)
	fmt.Println(cache)
	return ans
}

//      -1
//    2   3
//  1   -1   3

func main() {

	// traingle := [][]int{{-1}, {2, 3}, {1, -1, -3}}
	traingle := [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}

	answer := minimumTotal(traingle)

	fmt.Println("traningle : ", answer)

}
