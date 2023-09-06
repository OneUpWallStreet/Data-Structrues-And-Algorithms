# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        bad = float('inf')

        def bs(l,r):
            nonlocal bad
            if l <= r:
                mid = l + (r-l)//2
                if isBadVersion(mid):
                    bad = min(bad,mid)
                    bs(l,mid-1)
                else:
                    bs(mid+1,r)            

        bs(1,n)

        return bad

        