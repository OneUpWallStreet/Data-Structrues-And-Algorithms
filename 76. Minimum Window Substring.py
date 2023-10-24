class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t): return ""
        
        tMap = collections.defaultdict(int)
        sMap = collections.defaultdict(int)

        for ch in t: tMap[ch] += 1

        same = 0
        result = [float('inf'),(0,0)]

        l = r = 0

        while r < len(s):

            sMap[s[r]] += 1

            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]: same += 1
            while same == len(tMap):
                
                if result[0] > (r-l) + 1: 
                    result = [(r-l)+1,(l,r)]
                sMap[s[l]] -= 1

                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:  same -= 1
                
                l += 1
            
            r += 1

        if result[0] != float('inf'): return s[result[1][0]:result[1][1]+1]
        else: return ""

