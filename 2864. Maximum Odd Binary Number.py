class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hm = Counter(s)
        result = ["0"]*len(s)
        result[len(s)-1] = "1"
        i = 0
        while hm["1"] > 1:
            result[i] = "1"
            hm["1"] -= 1
            i += 1
        result[len(s)-1] = "1"
        return "".join(result) 

