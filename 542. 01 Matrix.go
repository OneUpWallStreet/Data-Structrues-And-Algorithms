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

type Node struct {
	x, y int
}

var rowCount int
var colCount int

var alreadyVisited map[Node]bool

func fetchValidPaths(mat [][]int, x, y int) []Node {

	validNodes := []Node{}

	// Go Right
	if y+1 < colCount && (mat[x][y+1] == 1 || mat[x][y+1] == 0) && alreadyVisited[Node{x, y + 1}] == false {
		validNodes = append(validNodes, Node{x, y + 1})
	}

	// Go Left
	if y-1 >= 0 && (mat[x][y-1] == 1 || mat[x][y-1] == 0) && alreadyVisited[Node{x, y - 1}] == false {
		validNodes = append(validNodes, Node{x, y - 1})
	}

	// Go Top
	if x-1 >= 0 && (mat[x-1][y] == 0 || mat[x-1][y] == 1) && alreadyVisited[Node{x - 1, y}] == false {
		validNodes = append(validNodes, Node{x - 1, y})
	}

	// Go Bottom
	if x+1 < rowCount && (mat[x+1][y] == 0 || mat[x+1][y] == 1) && alreadyVisited[Node{x + 1, y}] == false {
		validNodes = append(validNodes, Node{x + 1, y})
	}

	return validNodes
}

func depthFirstTraversal(mat [][]int, x, y, pathLen int) int {

	validPaths := fetchValidPaths(mat, x, y)

	if mat[x][y] == 0 || len(validPaths) == 0 {
		return pathLen
	}

	alreadyVisited[Node{x, y}] = true

	pathLen++

	var minPathLen int = math.MaxInt

	for i := 0; i < len(validPaths); i++ {
		minPathLen = min(minPathLen, depthFirstTraversal(mat, validPaths[i].x, validPaths[i].y, pathLen))
	}

	return minPathLen
}

func updateMatrix(mat [][]int) [][]int {

	rowCount = len(mat)
	colCount = len(mat[0])

	result := make([][]int, len(mat))

	copy(result, mat)

	for i := 0; i < len(mat); i++ {
		for j := 0; j < len(mat[i]); j++ {
			if mat[i][j] == 1 {
				alreadyVisited = map[Node]bool{}
				result[i][j] = depthFirstTraversal(mat, i, j, 0)
			} else {
				result[i][j] = 0
			}
		}
	}

	return result
}

func main() {

	mat := [][]int{{1, 1, 0, 0, 1, 0, 0, 1, 1, 0}, {1, 0, 0, 1, 0, 1, 1, 1, 1, 1}, {1, 1, 1, 0, 0, 1, 1, 1, 1, 0}, {0, 1, 1, 1, 0, 1, 1, 1, 1, 1}, {0, 0, 1, 1, 1, 1, 1, 1, 1, 0}, {1, 1, 1, 1, 1, 1, 0, 1, 1, 1}, {0, 1, 1, 1, 1, 1, 1, 0, 0, 1}, {1, 1, 1, 1, 1, 0, 0, 1, 1, 1}, {0, 1, 0, 1, 1, 0, 1, 1, 1, 1}, {1, 1, 1, 0, 1, 0, 1, 1, 1, 1}}

	answer := updateMatrix(mat)

	fmt.Println(answer)

	// fmt.Println("Hello World")
}

// [1,0,1,1,0,0,1,0,0,1]
// [0,1,1,0,1,0,1,0,1,1]
// [0,0,1,0,1,0,0,1,0,0]
// [1,0,1,0,1,1,1,1,1,1]
// [0,1,0,1,1,0,0,0,0,1]
// [0,0,1,0,1,1,1,0,1,0]
// [0,1,0,1,0,1,0,0,1,1]
// [1,0,0,0,1,1,1,1,0,1]
// [1,1,1,1,1,1,1,0,1,0]
// [1,1,1,1,0,1,0,0,1,1]
