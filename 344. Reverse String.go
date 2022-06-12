package main

func swap(i, j int, s []byte) {
	temp := s[i]
	s[i] = s[j]
	s[j] = temp
}

func reverseString(s []byte) {

	i := 0
	j := len(s) - 1

	for i < j {
		swap(i, j, s)
		i++
		j--
	}

}

func main() {

}
