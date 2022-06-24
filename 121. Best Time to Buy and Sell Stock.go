package main

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxProfit(prices []int) int {

	i := 0
	j := 0
	profit := 0

	for j < len(prices) {
		profit = max(prices[j]-prices[i], profit)

		if prices[i] > prices[j] {
			i++
		} else {
			j++
		}
	}

	return profit
}
