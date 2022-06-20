package main

func didFind(freqMap map[string]int, word string) bool {
	_, didFind := freqMap[word]
	return didFind
}

func countWords(words1 []string, words2 []string) int {

	freqMap1 := map[string]int{}
	freqMap2 := map[string]int{}
	output := 0

	wordMap := map[string]bool{}

	for i := 0; i < len(words1); i++ {
		if _, didFind := freqMap1[words1[i]]; didFind {
			freqMap1[words1[i]]++
		} else {
			freqMap1[words1[i]] = 1
			wordMap[words1[i]] = true
		}
	}

	for i := 0; i < len(words2); i++ {
		if _, didFind := freqMap2[words2[i]]; didFind {
			freqMap2[words2[i]]++
		} else {
			freqMap2[words2[i]] = 1

			if _, didFind := wordMap[words2[i]]; !didFind {
				wordMap[words2[i]] = true
			}

		}
	}

	for key, _ := range wordMap {
		if didFind(freqMap1, key) && didFind(freqMap2, key) && freqMap1[key] == 1 && freqMap2[key] == 1 {
			output++
		}
	}

	return output

}

func main() {

}
