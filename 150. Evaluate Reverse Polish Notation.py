class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(p1,p2,sign) -> int:
            if sign == "+": return p1+p2
            elif sign == "-": return p1-p2
            elif sign == "*": return p1*p2
            elif sign == "/": return int(p1/p2)
            
        s = collections.deque()

        for ch in tokens:
            if ch.lstrip('-').isdigit(): s.append(int(ch))
            else:
                p2 = s.pop()
                p1 = s.pop()
                val = calc(p1,p2,ch)
                s.append(val)
        
        return s.pop()
                