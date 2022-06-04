package main

import "fmt"

var result [][]string

func addBoardToResult(board [][]string) {

	newBoard := []string{}

	for i := 0; i < len(board); i++ {
		rowStr := ""
		for j := 0; j < len(board[i]); j++ {
			rowStr = rowStr + board[i][j]
		}
		newBoard = append(newBoard, rowStr)
	}

	result = append(result, newBoard)
}

func backTrack(colSet, posDiagSet, negDiagSet map[int]bool, row, n int, board [][]string) {

	if row == n {
		addBoardToResult(board)
		return
	}

	for col := 0; col < n; col++ {
		if colSet[col] || posDiagSet[col+row] || negDiagSet[row-col] {
			continue
		} else {
			colSet[col] = true
			board[row][col] = "Q"
			posDiagSet[col+row] = true
			negDiagSet[row-col] = true
			backTrack(colSet, posDiagSet, negDiagSet, row+1, n, board)

			colSet[col] = false
			posDiagSet[col+row] = false
			negDiagSet[row-col] = false
			board[row][col] = "."
		}
	}
}

func initBoard(n int) [][]string {
	board := [][]string{}
	for i := 0; i < n; i++ {
		row := []string{}
		for j := 0; j < n; j++ {
			row = append(row, ".")
		}
		board = append(board, row)
	}
	return board
}

func solveNQueens(n int) [][]string {
	colSet := map[int]bool{}
	posDiagSet := map[int]bool{}
	negDiagSet := map[int]bool{}
	result = [][]string{}

	board := initBoard(n)

	backTrack(colSet, posDiagSet, negDiagSet, 0, n, board)
	return result
}

func main() {
	ans := solveNQueens(4)
	fmt.Println(ans)
}
