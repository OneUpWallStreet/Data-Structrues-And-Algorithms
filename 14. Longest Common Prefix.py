class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        cur = ""
        minStr = 200
        for s in strs:
            minStr = min(minStr,len(s))

        for i in range(minStr):
            cur = strs[0][i]
            for word in strs:
                if word[i] != cur:
                    return result
            
            result = result + cur
        return result