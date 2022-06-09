package main

import "fmt"

func twoSum(numbers []int, target int) []int {

	i := 0
	j := len(numbers) - 1
	result := []int{}
	for i < j {
		if numbers[i]+numbers[j] == target {
			result = append(result, i+1)
			result = append(result, j+1)
			break
		} else if numbers[i]+numbers[j] < target {
			i++
		} else {
			j--
		}

	}
	return result

}

func main() {

	fmt.Println("Hello World")

}
