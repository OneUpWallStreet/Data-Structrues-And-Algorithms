class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        result = [0]*len(nums)
        cur = 1

        #Calculate prefix 
        for index in range(len(nums)):
            cur = cur*nums[index]
            prefix[index] = cur

        cur = 1
        #Calculate postfix
        for index in range(len(nums)-1,-1,-1):
            cur = cur*nums[index]
            postfix[index] = cur

        for index in range(len(nums)):
            if index != 0 and index != len(nums)-1:
                result[index] = prefix[index-1]*postfix[index+1]
            elif index == 0:
                result[index] = postfix[index+1]
            elif index == len(nums)-1:
                result[index] = prefix[index-1]
        
        return result