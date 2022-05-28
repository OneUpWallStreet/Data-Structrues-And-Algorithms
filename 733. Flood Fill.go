package main

import (
	"fmt"
)

type Node struct {
	x int
	y int
}

func nextValidNodes(image *[][]int, node Node, oldColor int, alreadyVisited map[Node]bool) []Node {

	var validNodes []Node

	// Go Bottom
	if node.x+1 < len(*image) && (*image)[node.x+1][node.y] == oldColor && alreadyVisited[Node{node.x + 1, node.y}] == false {
		validNodes = append(validNodes, Node{node.x + 1, node.y})
	}

	// Go Top
	if node.x-1 >= 0 && (*image)[node.x-1][node.y] == oldColor && alreadyVisited[Node{node.x - 1, node.y}] == false {
		validNodes = append(validNodes, Node{node.x - 1, node.y})
	}

	// Go Right
	if node.y+1 < len((*image)[node.x]) && (*image)[node.x][node.y+1] == oldColor && alreadyVisited[Node{node.x, node.y + 1}] == false {
		validNodes = append(validNodes, Node{node.x, node.y + 1})
	}

	// Go Left
	if node.y-1 >= 0 && (*image)[node.x][node.y-1] == oldColor && alreadyVisited[Node{node.x, node.y - 1}] == false {
		validNodes = append(validNodes, Node{node.x, node.y - 1})
	}

	return validNodes

}

func depthFirstSearch(image *[][]int, node Node, oldColor int, newColor int, alreadyVisited map[Node]bool) {

	(*image)[node.x][node.y] = newColor

	nextNodes := nextValidNodes(image, node, oldColor, alreadyVisited)
	alreadyVisited[node] = true

	if len(nextNodes) == 0 {
		return
	}

	for i := 0; i < len(nextNodes); i++ {
		depthFirstSearch(image, nextNodes[i], oldColor, newColor, alreadyVisited)
	}

}

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	depthFirstSearch(&image, Node{sr, sc}, image[sr][sc], newColor, map[Node]bool{})
	return image
}

func main() {
	var input = [][]int{{0, 0, 0}, {0, 0, 0}}
	answer := floodFill(input, 0, 0, 2)
	fmt.Println("Slice: ", answer)
}
