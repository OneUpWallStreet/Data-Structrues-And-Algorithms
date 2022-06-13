package main

import (
	"fmt"
	"math"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
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

func recursiveTraversal(traingle [][]int, rowIndex, colIndex, curSum int) int {
	curSum += traingle[rowIndex][colIndex]
	rowIndex++
	if rowIndex >= len(traingle) {
		fmt.Println(curSum)
		return curSum
	}
	nextCells := fetchNextCells(traingle[rowIndex], colIndex)
	var minRes int = math.MaxInt64
	for i := 0; i < len(nextCells); i++ {
		minRes = min(recursiveTraversal(traingle, rowIndex, nextCells[i], curSum), minRes)
	}
	return minRes
}

func minimumTotal(triangle [][]int) int {
	return recursiveTraversal(triangle, 0, 0, 0)
}

//      -1
//    2   3
//  1   -1   3

func main() {

	traingle := [][]int{{-1}, {2, 3}, {1, -1, -3}}

	answer := minimumTotal(traingle)

	fmt.Println("traningle : ", answer)

}
