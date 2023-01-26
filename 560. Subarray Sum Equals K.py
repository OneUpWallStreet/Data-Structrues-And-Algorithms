class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        curSum = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        for num in nums:
            curSum += num
            if curSum - k in prefixSum:
                result += prefixSum[curSum-k]
            prefixSum[curSum] += 1

        return result