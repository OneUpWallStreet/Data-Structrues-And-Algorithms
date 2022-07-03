import collections

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sStack = collections.deque()
        tStack = collections.deque()
        
        for c in s:
            if c == "#":
                if len(sStack) > 0:
                    sStack.pop()
            else:
                sStack.append(c)

                
        for c in t:
            if c == "#":
                if len(tStack) > 0:
                    tStack.pop()
            else:
                tStack.append(c)

        
        return sStack == tStack