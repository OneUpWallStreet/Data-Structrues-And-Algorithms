package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func selectMinFromRow(row []int, index int) (int, int) {
	if index+1 >= len(row) {
		return row[index], index
	} else if row[index] < row[index+1] {
		return row[index], index
	} else {
		return row[index+1], index + 1
	}
}

func minimumTotal(triangle [][]int) int {

	result := triangle[0][0]
	currentIndex := 0
	var minElement int

	for i := 1; i < len(triangle); i++ {
		row := triangle[i]
		minElement, currentIndex = selectMinFromRow(row, currentIndex)
		result += minElement
	}

	return result
}

func main() {

	traingle := [][]int{{-1}, {2, 3}, {1, -1, -3}}

	answer := minimumTotal(traingle)

	fmt.Println("traningle : ", answer)

}
