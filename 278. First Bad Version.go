package main

import (
	"fmt"
)

func isBadVersion(version int) bool

func firstBadVersion(n int) int {
	i := 0
	for i <= n {
		if isBadVersion(i) {
			return i
		}
		i++
	}
	return i
}

func main() {
	fmt.Println("Golang")
}
