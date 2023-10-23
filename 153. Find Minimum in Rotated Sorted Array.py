# Logic (from discussion tab)
# The main idea is, the element is said to be minimum in the rotated sorted array if the previous element to it is greater than it or there is no previous element(i.e. no rotation). We can do this using Binary search
# Find the mid element i.e. mid = (low+high)/2
# If the (mid+1)th element is less than mid element then return (mid+1)th element
# If the mid element is less than (mid-1)th element then return the mid element
# If the last element is greater than mid element then search in left half
# If the last element is less than mid element then search in right half

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