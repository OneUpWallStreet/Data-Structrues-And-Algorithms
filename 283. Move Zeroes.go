package main

func moveZeroes(nums []int) {

	i := 0
	j := 0

	for i < len(nums) && j < len(nums) {

		if nums[i] == 0 && nums[j] == 0 {
			j++
			continue
		}

		if nums[i] == 0 && nums[j] != 0 {
			nums[i] = nums[j]
			nums[j] = 0
		}

		i++
		j++

	}

}

func main() {

}
