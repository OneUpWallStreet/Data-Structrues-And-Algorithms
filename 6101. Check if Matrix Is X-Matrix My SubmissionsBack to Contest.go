package main

import "fmt"

type cell struct {
	x, y int
}

func contains(set map[cell]bool, num cell) bool {
	_, didFind := set[num]
	return didFind
}

func checkXMatrix(grid [][]int) bool {

	set := map[cell]bool{}

	// Check Positive Diagonal
	row := 0
	col := 0

	for row < len(grid) {
		if grid[row][col] == 0 {
			return false
		} else {
			set[cell{row, col}] = true
			row++
			col++

		}
	}

	row = len(grid) - 1
	col = 0

	for row >= 0 {
		if grid[row][col] == 0 {
			return false
		} else {
			set[cell{row, col}] = true
			row--
			col++
		}
	}

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if contains(set, cell{i, j}) {
				continue
			} else {
				if grid[i][j] != 0 {
					return false
				}
			}
		}
	}

	return true

}

func main() {

	input := [][]int{{2, 0, 0, 1}, {0, 3, 1, 0}, {0, 5, 2, 0}, {4, 0, 0, 2}}
	answer := checkXMatrix(input)
	fmt.Println("Answer: ", answer)

}
