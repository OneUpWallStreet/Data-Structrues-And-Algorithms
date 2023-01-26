class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        used = set()

        def twoSum(start,curSum):
            nonlocal result
            end = len(nums)-1
            while start < end:
                if nums[start] + curSum + nums[end] == 0:
                    triplet = [curSum,nums[start],nums[end]]
                    triplet.sort()
                    if (triplet[0],triplet[1],triplet[2]) not in used:
                        used.add((triplet[0],triplet[1],triplet[2]))
                        result.append(triplet)
                if nums[start] + curSum + nums[end] < 0:
                    start += 1
                else:
                    end -= 1

        for index in range(len(nums)):
            curSum = nums[index]
            twoSum(index+1,curSum)
        
        return result