class Solution:
    def defangIPaddr(self, address: str) -> str:        
        s = address.split(".")
        result = []
        for i,ch in enumerate(s): 
            result.append(ch)
            if i != len(s) - 1: result.append("[.]")
        return "".join(result)