package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func fetchPriceAfterDiscount(s string, discount int) string {
	s = strings.Replace(s, "$", "", -1)
	price, _ := strconv.ParseFloat(s, 64)
	discountedPrice := price - (price * float64(discount) / 100)
	return "$" + fmt.Sprintf("%.2f", discountedPrice)

}

func isPriceValid(price string) bool {
	if price[0] != '$' {
		return false
	}

	if len(price) == 1 {
		return false
	}

	dollarCount := 0
	for i := 0; i < len(price); i++ {

		if price[i] != '$' && !unicode.IsDigit(rune(price[i])) {
			return false
		}

		if price[i] == '$' {
			dollarCount++
		}
	}
	return dollarCount == 1
}

func discountPrices(sentence string, discount int) string {

	inputArray := strings.Split(sentence, " ")

	for i := 0; i < len(inputArray); i++ {
		if isPriceValid(inputArray[i]) {
			inputArray[i] = fetchPriceAfterDiscount(inputArray[i], discount)
		}
	}

	return strings.Join(inputArray, " ")
}

func main() {

	sentence := "there are $1 $2 and 5$ candies in the shop"
	discount := 50
	answer := discountPrices(sentence, discount)
	fmt.Printf("%v \n", answer)

}
