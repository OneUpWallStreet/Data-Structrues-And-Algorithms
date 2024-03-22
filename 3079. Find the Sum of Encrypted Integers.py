class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            maxNum = float('-inf')
            for ch in str(num): maxNum = max(int(ch),maxNum)
            result += int(str(maxNum)*len(str(num)))
        return result