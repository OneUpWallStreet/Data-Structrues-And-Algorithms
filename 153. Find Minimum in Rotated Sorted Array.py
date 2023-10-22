class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def bs(l, r):
            if l <= r:
                mid = l + (r -l) // 2
                if mid + 1 < len(nums) and nums[mid+1] < nums[mid]: 
                    return nums[mid+1]
                elif mid + 1 < len(nums) and nums[mid] < nums[mid+1] and nums[mid-1] > nums[mid]:
                    return nums[mid]
                if nums[mid] < nums[r]:
                    return bs(l,mid-1)
                else: return bs(mid+1,r)
        return bs(0, len(nums)-1)