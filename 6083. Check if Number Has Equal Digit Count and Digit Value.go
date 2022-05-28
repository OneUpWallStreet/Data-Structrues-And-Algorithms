package main

import (
	"fmt"
	"strconv"
)

func digitCount(num string) bool {

	freqMap := map[int]int{}

	for i := 0; i < len(num); i++ {
		value, _ := strconv.Atoi(string(num[i]))
		if _, didFind := freqMap[value]; didFind {
			freqMap[value]++
		} else {
			freqMap[value] = 1
		}
	}

	for i := 0; i < len(num); i++ {
		value, _ := strconv.Atoi(string(num[i]))
		if freqMap[i] != value {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Hello World")
	str := "1210"
	answer := digitCount(str)
	fmt.Println(answer)
}
