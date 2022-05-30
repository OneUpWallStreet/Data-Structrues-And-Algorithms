package main

import (
	"fmt"
	"sort"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func merge(intervals [][]int) [][]int {

	result := [][]int{}

	sort.Slice(intervals, func(i, j int) bool {
		// edge cases
		if len(intervals[i]) == 0 && len(intervals[j]) == 0 {
			return false // two empty slices - so one is not less than other i.e. false
		}
		if len(intervals[i]) == 0 || len(intervals[j]) == 0 {
			return len(intervals[i]) == 0 // empty slice listed "first" (change to != 0 to put them last)
		}

		// both slices len() > 0, so can test this now:
		return intervals[i][0] < intervals[j][0]
	})

	result = append(result, intervals[0])

	for i := 1; i < len(intervals); i++ {

		lastInterval := result[len(result)-1][1]
		start := intervals[i][0]
		end := intervals[i][1]

		if start <= lastInterval {
			result[len(result)-1][1] = max(end, lastInterval)
		} else {
			result = append(result, []int{start, end})
		}

	}

	return result
}

func main() {

	s := [][]int{{1, 4}, {0, 4}}

	answer := merge(s)
	fmt.Println("answer is: ", answer)

}
