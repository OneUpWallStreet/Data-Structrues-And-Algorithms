class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fz = nz = None
        for i in range(len(nums)):
            if nums[i] == 0: 
                fz = i
                break
        if fz == None: return
        for i in range(fz+1, len(nums)):
            if nums[i] != 0: 
                nz = i
                break
        if nz == None: return

        while fz < len(nums) and nz < len(nums):
            nums[fz] = nums[nz]
            if nz != fz: nums[nz] = 0
            while fz < len(nums) and nums[fz] != 0: fz += 1
            while nz < len(nums) and nums[nz] == 0: nz += 1

    