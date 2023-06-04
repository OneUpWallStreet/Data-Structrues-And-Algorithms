class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index in range(len(nums)): hashmap[nums[index]] = index
        for index in range(len(nums)):
            if (target - nums[index] in hashmap) and (hashmap[target - nums[index]] != index): 
                return [min(index,hashmap[target-nums[index]]),max(index,hashmap[target-nums[index]])]
        