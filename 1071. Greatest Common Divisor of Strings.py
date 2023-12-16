class Solution:

    # From NeetCode
    def Dev2023gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len1, len2 = len(str1), len(str2)

        def isDivisor(i):
            if len1 % len(str1[:i+1]) != 0 or len2 % len(str2[:i+1]) != 0: return None
            
            f1, f2 = len1 // len(str1[:i+1]), len2 // len(str2[:i+1])

            if (str1[:i+1] == str2[:i+1]) and (f1 * str1[:i+1] == str1 and f2 * str2[:i+1] == str2): return str1[:i+1]


        for i in range(min(len1,len2),-1,-1):
            cur = isDivisor(i)
            if cur != None: return cur
        return ""

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