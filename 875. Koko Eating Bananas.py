class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canKokoEat(k) -> bool:
            hLeft = h
            for pile in piles: hLeft -= ceil(pile/k)
            return hLeft >= 0

        result = float('inf')

        def bs(l,r):
            nonlocal result

            if l <= r:
                k = l + (r - l) // 2
                if canKokoEat(k): 
                    result = min(result,k)
                    bs(l,k-1)
                else:  bs(k+1,r)

        bs(1,max(piles))
        return result
        


                