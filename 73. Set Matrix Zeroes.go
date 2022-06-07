package main

import "fmt"

type Node struct {
	x, y int
}

func washRowAndColumns(matrix [][]int, node Node) {

	// Fill Row
	for col := 0; col < len(matrix[0]); col++ {
		matrix[node.x][col] = 0
	}

	// Fill Col
	for row := 0; row < len(matrix); row++ {
		matrix[row][node.y] = 0
	}

}

func setZeroes(matrix [][]int) {

	zeros := []Node{}
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 0 {
				zeros = append(zeros, Node{i, j})
			}
		}
	}

	for i := 0; i < len(zeros); i++ {
		washRowAndColumns(matrix, zeros[i])
	}

}

func main() {

	input := [][]int{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}
	setZeroes(input)
	fmt.Println(input)
}
