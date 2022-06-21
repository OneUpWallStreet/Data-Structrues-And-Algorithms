package main

import "fmt"

func didFind(wordMap map[byte]byte, ch byte) bool {
	_, didFind := wordMap[ch]
	return didFind
}

func isIsomorphic(s string, t string) bool {

	wordMap := map[byte]byte{}
	usedWords := map[byte]byte{}

	for i := 0; i < len(s); i++ {

		if !didFind(wordMap, s[i]) && !didFind(usedWords, t[i]) {
			wordMap[s[i]] = t[i]
			usedWords[t[i]] = t[i]
		} else if wordMap[s[i]] != t[i] {
			return false
		}

	}

	return true
}

func main() {
	answer := isIsomorphic("badc", "baba")
	fmt.Println("Answer: ", answer)
}
