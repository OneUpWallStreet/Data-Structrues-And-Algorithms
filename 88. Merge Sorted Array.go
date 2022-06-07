package main

import (
	"fmt"
)

func swap(i, j int, nums []int) {
	temp := nums[i]
	nums[i] = nums[j]
	nums[j] = temp
}

func merge(nums1 []int, m int, nums2 []int, n int) {

	var realIndex1 int

	for i := len(nums1) - 1; i >= 0; i-- {
		if nums1[i] != 0 {
			realIndex1 = i
			break
		}
	}

	j := len(nums1) - 1

	realIndex2 := len(nums2) - 1

	for realIndex1 >= 0 && realIndex2 >= 0 {
		if nums2[realIndex2] > nums1[realIndex1] {
			fmt.Printf("nums2[realIndex2] %v and realIndex2: %v and num1[realIndex1] : %v and real INdex 1 : %v \n", nums2[realIndex2], realIndex2, nums1[realIndex1], realIndex1)
			nums1[j] = nums2[realIndex2]
			realIndex2--
			fmt.Println(nums1)
		} else if {
			swap(realIndex1, j, nums1)
			realIndex1--
		}
		j--
	}

	fmt.Println("realIndex2: ", realIndex2)

	for realIndex2 >= 0 {
		nums1[j] = nums2[realIndex2]
		j--
		realIndex2--
	}

	fmt.Println(nums1)

}

func main() {

	merge([]int{-1, -1, 0, 0, 0, 0}, 3, []int{-1, 0}, 3)

	fmt.Println("hello")
}
