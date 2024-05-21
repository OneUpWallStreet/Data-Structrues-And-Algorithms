class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= goal: goal = i
        return True if goal == 0 else False
    
    # Bottom-up DP
    def canJumpDP(PDself, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2,-1,-1):
            maxJump = min(i+nums[i],len(nums)-1) 
            for j in range(i+1,maxJump+1):
                if dp[j]: 
                    dp[i] = True
                    break
        return dp[0]