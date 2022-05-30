package main

import (
	"fmt"
)

func canConstruct(ransomNote string, magazine string) bool {

	magFreq := map[byte]int{}

	for i := 0; i < len(magazine); i++ {
		if _, didFind := magFreq[magazine[i]]; didFind {
			magFreq[magazine[i]]++
		} else {
			magFreq[magazine[i]] = 1
		}
	}

	for i := 0; i < len(ransomNote); i++ {
		if _, didFind := magFreq[ransomNote[i]]; didFind {
			if magFreq[ransomNote[i]] > 0 {
				magFreq[ransomNote[i]]--
			} else {
				return false
			}
		} else {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Creit Sussie")
}
