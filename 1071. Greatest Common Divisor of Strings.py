class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        result = ""

        # Use the shorter string here, for now use str2
        for last in range(0,len(str2)):
            
            curStr = str2[:last+1]

            if len(str1) % len(curStr) != 0 or  len(str2) % len(curStr) != 0:
                continue

            
            if str1 == (curStr*int((len(str1)/len(curStr)))) and str2 == (curStr*int(len(str2)/len(curStr))):
                if len(curStr) > len(result): result = curStr

        
        return result