package main

import "strings"

func swap(i, j int, s []byte) {
	temp := s[i]
	s[i] = s[j]
	s[j] = temp
}

func reverseWord(s string) string {

	i := 0
	j := len(s) - 1
	byteArr := []byte(s)

	for i < j {
		swap(i, j, byteArr)
		i++
		j--
	}

	return string(byteArr)

}

func reverseWords(s string) string {

	strArray := strings.Split(s, " ")
	var output string

	for i := 0; i < len(strArray); i++ {
		strArray[i] = reverseWord(strArray[i])
	}

	output = strings.Join(strArray, " ")

	return output
}

func main() {

}
