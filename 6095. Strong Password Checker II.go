package main

import "unicode"

func doesContain(c byte, set map[byte]bool) bool {
	_, didFind := set[c]
	return didFind
}

func strongPasswordCheckerII(password string) bool {

	if len(password) < 8 {
		return false
	}

	digitSet := map[byte]bool{'0': true, '1': true, '2': true, '3': true, '4': true, '5': true, '6': true, '7': true, '8': true, '9': true}
	specialSet := map[byte]bool{'!': true, '@': true, '#': true, '$': true, '%': true, '^': true, '&': true, '*': true, '(': true, ')': true, '-': true, '+': true}

	containsLowerCase := false
	containsUpperCase := false
	containsDigit := false
	containsSpecial := false

	for i := 0; i < len(password); i++ {
		if unicode.IsUpper(rune(password[i])) {
			containsUpperCase = true
		}
		if unicode.IsLower(rune(password[i])) {
			containsLowerCase = true
		}
		if doesContain(password[i], digitSet) {
			containsDigit = true
		}
		if doesContain(password[i], specialSet) {
			containsSpecial = true
		}

	}

	if !(containsLowerCase && containsUpperCase && containsDigit && containsSpecial) {
		return false
	}

	for i := 0; i < len(password); i++ {
		if i < len(password)-1 && password[i] == password[i+1] {
			return false
		}
	}

	return true

}

func main() {

}
