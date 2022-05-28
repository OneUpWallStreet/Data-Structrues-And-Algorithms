package main

import (
	"fmt"
	"strings"
)

func largestWordCount(messages []string, senders []string) string {

	wordCount := map[string]int{}

	for i := 0; i < len(messages); i++ {
		count := len(strings.Split(messages[i], " "))

		if _, didFind := wordCount[senders[i]]; didFind {
			wordCount[senders[i]] += count
		} else {
			wordCount[senders[i]] = count
		}
	}

	maxCount := 0
	var bestSender string

	for sender, count := range wordCount {
		if count > maxCount {
			bestSender = sender
			maxCount = count
		} else if count == maxCount {
			if strings.Compare(sender, bestSender) == 1 {
				bestSender = sender
			}
		}
	}

	return bestSender
}

func main() {
	messages := []string{"How is leetcode for everyone", "Leetcode is useful for practice"}
	senders := []string{"Bob", "Charlie"}

	winner := largestWordCount(messages, senders)

	fmt.Println("Winner: ", winner)
}
