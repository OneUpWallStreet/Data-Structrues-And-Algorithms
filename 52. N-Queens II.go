package main

import (
	"fmt"
)

var counter int = 0

func backTrack(colSet, posDiagSet, negDiagSet map[int]bool, row, n int) {

	if row == n {
		counter++
		return
	}

	for col := 0; col < n; col++ {
		if colSet[col] || posDiagSet[col+row] || negDiagSet[row-col] {
			continue
		} else {
			colSet[col] = true
			posDiagSet[col+row] = true
			negDiagSet[row-col] = true
			backTrack(colSet, posDiagSet, negDiagSet, row+1, n)

			colSet[col] = false
			posDiagSet[col+row] = false
			negDiagSet[row-col] = false
		}
	}

}

func totalNQueens(n int) int {
	colSet := map[int]bool{}
	posDiagSet := map[int]bool{}
	negDiagSet := map[int]bool{}

	counter = 0

	backTrack(colSet, posDiagSet, negDiagSet, 0, n)

	fmt.Println("Counnter is: ", counter)

	return counter
}

func main() {
	fmt.Println("Hello World")
}
