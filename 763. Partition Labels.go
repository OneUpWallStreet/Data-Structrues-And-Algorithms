package main

import (
	"fmt"
)

func partitionLabels(s string) []int {

	freqMap := map[byte]bool{}

	result := []int{}
	counter := 0

	for i := 0; i < len(s); i++ {
		if freqMap[s[i]] == false {
			freqMap[s[i]] = true
			counter++
		} else {
			result = append(result, counter)
			counter = 0
			freqMap = map[byte]bool{}
		}
	}

	return result
}

func main() {
	fmt.Println("Warren Buffet")
}
