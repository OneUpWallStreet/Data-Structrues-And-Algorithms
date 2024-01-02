class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        hm = collections.Counter(nums)
        result = []

        while len(hm) > 0:
            vistied = set()
            cur = []
            iMap = deepcopy(hm)
            for k,v in iMap.items():
                cur.append(k)
                hm[k] -= 1
                if hm[k] == 0: del hm[k]
            result.append(cur)

        return result