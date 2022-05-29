package main

import (
	"fmt"
)

func rearrangeCharacters(s string, target string) int {

	freqMap := map[byte]int{}
	counter := 0

	for i := 0; i < len(s); i++ {
		if _, didFind := freqMap[s[i]]; didFind {
			freqMap[s[i]]++
		} else {
			freqMap[s[i]] = 1
		}
	}

out:
	for true {
		for i := 0; i < len(target); i++ {
			if _, didFind := freqMap[target[i]]; didFind {
				if freqMap[target[i]] > 0 {
					freqMap[target[i]]--
				} else {
					break out
				}
			} else {
				break out
			}
		}
		counter++

	}

	return counter

}

func main() {
	s := "ilovecodingonleetcode"
	target := "code"
	answer := rearrangeCharacters(s, target)
	fmt.Println("Answer is: ", answer)
}
