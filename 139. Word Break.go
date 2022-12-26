package main

import (
	"fmt"
)

func wordBreak(s string, wordDict []string) bool {

	dict := map[string]bool{}

	for i := 0; i < len(wordDict); i++ {
		dict[wordDict[i]] = false
	}

	word := ""
	wordCount := 0

	for i := 0; i < len(s); i++ {
		word = word + string(s[i])
		if _, didFind := dict[word]; didFind {
			dict[word] = true
			wordCount += len(word)
			word = ""
		}
	}

	if wordCount == len(s) {
		return true
	}

	fmt.Println(dict)

	for _, val := range dict {
		if val == false {
			return false
		}
	}

	return true
}

func main() {

	// Input: s = "leetcode",
	// Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

	// "aaaaaaa"
	// ["aaaa","aaa"]

	wordDict := []string{"aaaa", "aaa"}
	fmt.Println(wordBreak("aaaaaaa", wordDict))
}
