class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # No idea why this works?
        # This is constant memory solution
        # Coded it on my own, but it's not intuitive at all 
        nums.reverse()
        k = k % len(nums)

        def reverse(p1,p2):
            while p1 < p2:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                p1 += 1
                p2 -= 1
        
        p1, p2 = 0, k-1
        reverse(p1,p2)

        p1, p2 = k, len(nums)-1
        reverse(p1,p2)

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

