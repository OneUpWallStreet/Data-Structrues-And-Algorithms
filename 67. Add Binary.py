class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        result = ""
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = int(a[i]) if i < len(a) else 0 
            digitB = int(b[i]) if i < len(b) else 0

            val = digitA + digitB + carry

            if val == 2: val, carry = 0,1
            elif val == 3: carry = val = 1
            else: carry = 0
            
            result =  str(val) + result

        if carry == 1: result = str(carry) + result
        return result