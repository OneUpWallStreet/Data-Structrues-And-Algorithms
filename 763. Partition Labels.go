package main

import (
	"fmt"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func partitionLabels(s string) []int {

	freqMap := map[byte]int{}
	result := []int{}

	// Init map to keep track of last element
	for i := 0; i < len(s); i++ {
		freqMap[s[i]] = i
	}

	size := 0
	end := freqMap[s[0]]

	for i := 0; i < len(s); i++ {
		size++
		end = max(end, freqMap[s[i]])

		if i == end {
			result = append(result, size)
			size = 0
		}

	}

	return result
}

func main() {

	answer := partitionLabels("ababcbacadefegdehijhklij")
	fmt.Println("Answer : ", answer)

	fmt.Println("Warren Buffet")
}
