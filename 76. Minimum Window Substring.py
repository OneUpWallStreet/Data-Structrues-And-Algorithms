class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        result = None

        tMap = Counter(t)

        hm = collections.defaultdict(int)  

        same = l = r = 0

        while r < len(s):
            
            ch = s[r]
            hm[ch] += 1

            if hm[ch] == tMap[ch]: same += 1

            while same == len(tMap):

                if not result or (r-l) + 1 < len(result):
                    result = s[l:r+1]

                hm[s[l]] -= 1

                if hm[s[l]] < tMap[s[l]]: same -= 1
                l += 1

            r += 1
        return result if result else ""
