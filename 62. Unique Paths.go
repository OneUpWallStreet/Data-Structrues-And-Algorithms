package main

import "fmt"

var cache map[Cell]int

type Cell struct {
	x, y int
}

func didHitCache(row, col int) bool {
	_, didFind := cache[Cell{row, col}]
	return didFind
}

func dynamicProgramming(m, n int) int {
	if didHitCache(m, n) {
		return cache[Cell{m, n}]
	} else if m == 1 && n == 1 {
		return 1
	} else if m == 0 || n == 0 {
		return 0
	} else {
		left := dynamicProgramming(m-1, n)
		right := dynamicProgramming(m, n-1)
		cache[Cell{m, n}] = left + right
		return cache[Cell{m, n}]
	}
}

func uniquePaths(m int, n int) int {
	cache = map[Cell]int{}
	return dynamicProgramming(m, n)
}

func main() {
	ans := uniquePaths(35, 35)
	fmt.Println(ans)
}
