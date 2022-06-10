package main

import "fmt"

var cache map[Cell]int
var totalCols int
var totalRows int

type Cell struct {
	x, y int
}

func didHitCache(row, col int) bool {
	_, didFind := cache[Cell{row, col}]
	return didFind
}

func fetchNextCells(row, col int) []Cell {

	nextCells := []Cell{}

	// Go top
	if row-1 >= 0 {
		nextCells = append(nextCells, Cell{row - 1, col})
	}

	if col-1 >= 0 {
		nextCells = append(nextCells, Cell{row, col - 1})
	}

	return nextCells
}

func dynamicProgramming(row, col, path int) {

	path++

	if didHitCache(row, col) {
		return
	}

	nextCells := fetchNextCells(row, col)

	if len(nextCells) == 0 {
		fmt.Println("pathLen: ", path)
		fmt.Printf("Row: %v and Col: %v", row, col)
		cache[Cell{row, col}] = path
		return
	}

	for i := 0; i < len(nextCells); i++ {
		dynamicProgramming(nextCells[i].x, nextCells[i].y, path)
	}

}

func uniquePaths(m int, n int) int {
	cache = map[Cell]int{}
	dynamicProgramming(3, 7, 0)
	fmt.Println(cache)
	return 0
}

func main() {
	ans := uniquePaths(3, 7)
	fmt.Println(ans)
}
