class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        hm = collections.defaultdict(int)
        result = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i]*nums[j]
                if prod in hm: result += hm[prod]
                hm[prod] += 1
            
        return result*8
        