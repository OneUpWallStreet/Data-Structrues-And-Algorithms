from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def bs(l,r):

            if l <= r:

                mid = l + (r - l) //2

                if nums[mid] == target: return mid

                # Check if we are in left part of the array or right
                # We are in left
                if nums[l] <= nums[mid]:
                    # Target is greater then max value on left subarray
                    if target > nums[mid]: return bs(mid+1,r)
                    # Target is less then least value on left subarray
                    elif target < nums[l]: return bs(mid+1,r) 
                    # Target is present in left subarray
                    else: return bs(l,mid-1)
                # Else we are in right sorted portion
                else:
                    # If target is greater than max number on subarray 
                    if target > nums[r]: return bs(l,mid-1)
                    #  Target is less then middle, so we just look at left portion of subarray
                    elif target < nums[mid]: return bs(l,mid-1)
                    # Target is present in right portion of subarray
                    else: return bs(mid+1,r)
                    
            return -1
        
        return bs(0,len(nums)-1)
    
    # Solved this by building on top of the problem -> 153. Find Minimum in Rotated Sorted Array
    def searchCustom(self, nums: List[int], target: int) -> int:
        

        l, r, pivotIndex = 0, len(nums) - 1, -1

        def bs(l, r):
            if l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target: return mid
                elif nums[mid] < target: return bs(mid+1,r)
                else: return bs(l,mid-1)
            return -1
            

        while l <= r:
            mid = l + (r-l) // 2
            if mid + 1 < len(nums) and nums[mid+1] < nums[mid]:
                pivotIndex = mid+1
                break
            elif mid + 1 < len(nums) and nums[mid] < nums[mid+1] and nums[mid-1] > nums[mid]:
                pivotIndex = mid
                break

            if nums[mid] < nums[r]: r = mid - 1
            else:  l = mid + 1

        if pivotIndex == -1 or pivotIndex == 0: return bs(0,len(nums) - 1)
        else:
            if nums[len(nums)-1] >= target:
                return bs(pivotIndex,len(nums)-1)
            else: return bs(0,pivotIndex)



    # This is the best solution according to me lol
    def BetterSolutionsearch(self, nums: List[int], target: int) -> int:
        
        pi = 0
        minNumber = float('inf')
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < minNumber: 
                minNumber = nums[mid]
                pi = mid
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid - 1

        def bs(l,r):
            if l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target: return mid
                elif nums[mid] < target: return bs(mid+1,r)
                else: return bs(l,mid-1)
            return -1

        if pi == 0: return bs(0,len(nums)-1)

        if target >= nums[pi] and target <= nums[len(nums)-1]: return bs(pi,len(nums)-1)
        else: return bs(0,pi)
