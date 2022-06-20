package main

import "fmt"

var result = []string{}

func recursiveTraversal(open, closed int, parenthesisString string) {

	if open == 0 && closed == 0 {
		result = append(result, parenthesisString)
	}
	// Allowed to use closing parenthesis
	if closed > open {
		recursiveTraversal(open, closed-1, parenthesisString+")")
	}

	if open > 0 {
		recursiveTraversal(open-1, closed, parenthesisString+"(")
	}

}

func generateParenthesis(n int) []string {
	result = []string{}
	recursiveTraversal(n, n, "")
	return result
}

func main() {
	answer := generateParenthesis(3)
	fmt.Println("Answer Count: ", len(answer))
	fmt.Println(answer)
}
