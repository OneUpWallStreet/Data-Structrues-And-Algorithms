class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        fMap,result = defaultdict(int), 0
        for ch in s: fMap[ch] += 1

        curOdd = 0

        for k,v in fMap.items():
            if v % 2 == 0: 
                result += v
                continue
            if v > curOdd:
                if curOdd != 0:
                    result -= 1
                curOdd = v
                result += v
            else:
                result += v - 1

        return result

