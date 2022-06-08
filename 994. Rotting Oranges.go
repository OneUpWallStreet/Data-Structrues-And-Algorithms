package main

import "fmt"

type Cell struct {
	x, y int
}

// Returns row,col
func fetchFreshOrangesToRot(x, y int, grid [][]int) []Cell {

	freshOranges := []Cell{}

	// Go Left
	if y-1 >= 0 && grid[x][y-1] == 1 {
		freshOranges = append(freshOranges, Cell{x, y - 1})
	}

	// Go Right
	if y+1 < len(grid[x]) && grid[x][y+1] == 1 {
		freshOranges = append(freshOranges, Cell{x, y + 1})
	}

	// Go Top
	if x-1 >= 0 && grid[x-1][y] == 1 {
		freshOranges = append(freshOranges, Cell{x - 1, y})
	}

	// Go Botttom
	if x+1 < len(grid) && grid[x+1][y] == 1 {
		freshOranges = append(freshOranges, Cell{x + 1, y})
	}

	return freshOranges
}

func areThereFreshOranges(grid [][]int) bool {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				return true
			}
		}
	}
	return false
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func rotOrange(x, y, time int, grid [][]int, set map[Cell]bool) int {
	grid[x][y] = 2

	// No Fresh Oranges
	if !areThereFreshOranges(grid) {
		return time
	}

	freshOranges := fetchFreshOrangesToRot(x, y, grid)

	minTime := time

	for i := 0; i < len(freshOranges); i++ {
		if _, didFind := set[Cell{freshOranges[i].x, freshOranges[i].y}]; didFind {
			continue
		}
		set[Cell{freshOranges[i].x, freshOranges[i].y}] = true
		minTime = min(rotOrange(freshOranges[i].x, freshOranges[i].y, time, grid, set), minTime)
	}

	return minTime
}

func orangesRotting(grid [][]int) int {
	rotOrange(0, 0, grid, map[Cell]bool{})
	if areThereFreshOranges(grid) {
		return -1
	}
	return time
}

func main() {
	grid := [][]int{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}
	ans := orangesRotting(grid)
	fmt.Println("Answer: ", ans)
}
