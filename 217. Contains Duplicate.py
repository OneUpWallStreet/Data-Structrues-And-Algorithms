class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Solution 1 - Sorting
        # O(1) - Space
        # O(nlogn) - Time

        nums.sort()

        for index in range(len(nums)):
            if index == len(nums) - 1: return False
            if nums[index] == nums[index+1]: return True


        # Solution 2 - Hashtable
        # O(n) - Space
        # O(n) - Time

        hashset = set()

        for num in nums:
            if num in hashset: return True
            else: hashset.add(num)

        return False




