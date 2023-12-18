from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        res = []
        i = 0

        while i < len(chars):
            res.append(chars[i])
            cur = i 
            i += 1

            while i < len(chars) and chars[i] == chars[i-1]: i += 1

            if i - cur == 1: continue
            else: 
                count = i - cur
                for intCh in str(count): res.append(intCh)
                
        for i in range(min(len(chars),len(res))):
            chars[i] = res[i]
            i += 1            
        return len(res)
