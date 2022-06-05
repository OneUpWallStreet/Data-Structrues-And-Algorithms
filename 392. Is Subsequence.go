package main

import (
	"fmt"
)

func isSubsequence(s string, t string) bool {

	i := 0
	j := 0

	for j < len(t) && i < len(s) {
		if t[j] == s[i] {
			i++
		}
		j++
	}

	// fmt.Println("i == :", i)
	// fmt.Println("j == : ", j)

	// fmt.Println("len(s)-1: ", len(s)-1)

	return i == len(s)

}

func main() {

	// Input: s = "abc", t = "ahbgdc"

	ans := isSubsequence("abc", "ahbgdc")

	fmt.Println("answer : ", ans)

	fmt.Println("Hello World")
}
