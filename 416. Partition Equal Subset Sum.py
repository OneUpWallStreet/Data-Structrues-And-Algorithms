class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums) / 2
        cache = dict()

        def rcr(index,curSum):
            
            if curSum == target: 
                return True
            elif curSum > target: return False
            elif index >= len(nums): return False
            elif (index,curSum) in cache: return cache[(index,curSum)]

            # Use current element
            if rcr(index+1,curSum + nums[index]): return True

            # Ignore current element
            if rcr(index+1,curSum): return True

            cache[(index,curSum)] = False

            return False
        
        return rcr(0,0)
