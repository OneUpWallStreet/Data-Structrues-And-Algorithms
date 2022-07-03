import collections

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = collections.deque()
        
        for c in s:
            
            if c != "]":
                stack.append(c)
            else:
                curString = ""
                while stack[-1] != "[":
                    curString =  stack.pop() + curString
                
                stack.pop()
                digit = ""

                while len(stack) != 0 and stack[-1].isdigit():
                    digit = stack.pop() + digit
                    
                
                stack.append(curString*int(digit))
        
        print(stack)
        return "".join(stack)
