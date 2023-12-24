class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        arr = []
        l, r = 0, 1

        while r < len(nums):
            arr.append(nums[r])
            arr.append(nums[l])
            l += 2
            r += 2
        return arr