package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func recursiveTraversal(heights []int, index, brick, ladders int) int {

	if index+1 == len(heights) || (((heights[index+1]-heights[index]) > brick && ladders == 0) && heights[index+1] > heights[index]) {
		return index
	}

	if heights[index+1] < heights[index] {
		return recursiveTraversal(heights, index+1, brick, ladders)
	}

	var maxSum int

	if (heights[index+1] - heights[index]) < brick {
		maxSum = max(maxSum, recursiveTraversal(heights, index+1, brick-(heights[index+1]-heights[index]), ladders))
	}

	if ladders > 0 {
		maxSum = max(maxSum, recursiveTraversal(heights, index+1, brick, ladders-1))
	}
	return maxSum
}

func furthestBuilding(heights []int, bricks int, ladders int) int {
	return recursiveTraversal(heights, 0, bricks, ladders)
}

func main() {

	heights := []int{4, 12, 2, 7, 3, 18, 20, 3, 19}
	bricks := 10
	ladders := 2

	answer := furthestBuilding(heights, bricks, ladders)

	fmt.Println("Answer: ", answer)

}
