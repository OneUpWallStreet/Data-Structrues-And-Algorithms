package main

import (
	"fmt"
)

func didFindChar(c byte, hashmap map[byte]bool) bool {
	_, didFind := hashmap[c]
	return didFind
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func lengthOfLongestSubstring(s string) int {
	hashmap := map[byte]bool{}
	i := 0
	j := 0
	output := 0

	for j < len(s) {
		for didFindChar(s[j], hashmap) {
			hashmap[s[j]] = false
			i++
		}
		hashmap[s[j]] = true
		output = max(j-i, output)
		j++

	}

	return output
}

func main() {
	ans := lengthOfLongestSubstring("abcabcbb")
	fmt.Println("Answer: ", ans)
}

// func lengthOfLongestSubstring(s string) int {
// 	hashmap := map[byte]int{}
// 	i := 0
// 	result := 0

// 	for i < len(s) {

// 		if didFindChar(s[i], hashmap) {
// 			result = i
// 		}
// 		hashmap[s[i]] = i
// 		i++
// 	}

// 	return i - result
// }

// hashmap := map[byte]int{}
// i := 0
// maxOutput := 0
// result := 0

// for i < len(s) {

// 	if didFindChar(s[i], hashmap) {
// 		maxOutput = max(i-result, maxOutput)
// 		result = hashmap[s[i]] + 1
// 	}
// 	hashmap[s[i]] = i
// 	i++
// }

// return max(maxOutput, (i-1)-result)

// hashmap := map[byte]int{}
// i := 0
// j := 0
// output := 0

// for j < len(s) {
// 	if didFindChar(s[j], hashmap) {

// 		i = hashmap[s[hashmap[s[j]]+1]]
// 	}
// 	hashmap[s[j]] = j
// 	j++
// 	output = max(output, j-i)
// }

// return output
