class Solution:
    def totalMoney(self, n: int) -> int:
        result = cur = 0
        for i in range(n):
            if i % 7 == 0: cur += 1
            result += cur + (i % 7) 
        return result