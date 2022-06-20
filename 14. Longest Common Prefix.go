package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func countSmallestChar(strs []string) int {
	smallestLen := len(strs[0])
	for i := 0; i < len(strs); i++ {
		smallestLen = min(smallestLen, len(strs[i]))
	}
	return smallestLen
}

func longestCommonPrefix(strs []string) string {
	answer := ""

	minLen := countSmallestChar(strs)

	for i := 0; i < minLen; i++ {
		currentChar := strs[0][i]
		for j := 1; j < len(strs); j++ {
			if strs[j][i] != currentChar {
				return answer
			}
		}
		answer = answer + string(currentChar)
	}

	return answer
}

func main() {

	strs := []string{"flower", "flow", "flight"}
	answer := longestCommonPrefix(strs)
	fmt.Println("Answer: ", answer)
}
