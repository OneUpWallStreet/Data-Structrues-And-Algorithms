class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        l, r = 0, 2
        result = [float('-inf'),""]

        while r < len(num):
            if (num[l] == num[l+1]) and (num[l+1] == num[r]) and (int(num[l:r+1]) > result[0]): 
                result[1] = num[l:r+1]
                result[0] = int(num[l:r+1])
            l += 1
            r += 1
        
        return result[1]