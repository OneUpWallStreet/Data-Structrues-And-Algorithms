class Solution:

    def topDownDPRob(self, nums: List[int]) -> int:

        cache = dict()

        def rcr(index):    
            if index in cache: return cache[index]
            elif index >= len(nums): return 0
            cache[index] = max(rcr(index+1),rcr(index+2) + nums[index])
            return cache[index] 
        return rcr(0)

    def iterativeRob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2