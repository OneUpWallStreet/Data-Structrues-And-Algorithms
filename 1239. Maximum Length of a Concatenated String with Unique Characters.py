class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        result = 0

        def check(s):
            nonlocal result
            hs = set()
            for ch in s:
                if ch in hs: 
                    return 
                hs.add(ch)
            result = max(result, len(s))

        def rcr(index,s):
            if index >= len(arr): 
                check(s)
                return
            
            # skip cur string 
            rcr(index+1,s)

            # use cur
            rcr(index+1,s + arr[index])

        rcr(0,"")
        return result

        