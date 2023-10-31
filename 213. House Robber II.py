class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = dict()
        def rcr(index,lastIndex):
            if index in cache: return cache[index]
            elif index > lastIndex: return 0
            cache[index] = max(rcr(index+1,lastIndex), rcr(index+2,lastIndex) + nums[index])
            return cache[index]
        rob1 = rcr(0,len(nums)-2)
        cache = dict()
        rob2 = rcr(1,len(nums)-1)
        return max(rob1,rob2)