package main

func longestPalindrome(s string) int {

	freqMap := map[byte]int{}

	for i := 0; i < len(s); i++ {
		freqMap[s[i]]++
	}

	result := 0

	for _, value := range freqMap {
		result += value / 2 * 2
		if result%2 == 0 && value%2 == 1 {
			result += 1
		}
	}

	return result
}
