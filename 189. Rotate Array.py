class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        def reverseArr(l,r):
            while l < r:
                temp = nums[l] 
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        
        reverseArr(0,len(nums)-1)

        reverseArr(0,k-1)
        reverseArr(k,len(nums)-1)


    def rotateLinearMemorySolution(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        newArr = [-1] * len(nums)

        def getNewIndex(index) -> int:
            if (index + k) < len(nums): return index + k
            else: return (index + k) % len(nums)

        for i in range(len(nums)): newArr[getNewIndex(i)] = nums[i]
        
        for i in range(len(nums)): nums[i] = newArr[i]

