class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        result, found = float('inf'), False

        def dfs(i, curSum, counter):
            nonlocal result, found

            if i >= len(coins): return
            elif curSum == amount: 
                found = True
                result = min(result, counter)
                return
            elif curSum > amount: return
            
            curSum += coins[i]
            dfs(i, curSum, counter + 1)
            dfs(i + 1, curSum, counter + 1)
            curSum -= coins[i]
            dfs(i + 1, curSum, counter)

        dfs(0, 0, 0)

        if not found: return -1
        return result