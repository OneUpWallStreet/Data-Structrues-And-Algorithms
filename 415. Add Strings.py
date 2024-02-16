class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        p1, p2 = len(num1) - 1, len(num2) - 1
        result = ""
        carry = 0

        while p1 >= 0 and p2 >= 0:

            cur = int(num1[p1]) + int(num2[p2]) + carry
            if cur > 9: 
                cur = str(cur)
                carry = int(cur[0])
                result = result + cur[1]
            else: 
                carry = 0
                result = result + str(cur)
            p1 -= 1
            p2 -= 1

        while p1 >= 0:
            val = carry + int(num1[p1])
            if val > 9:
                val = str(val)
                carry = int(val[0])
                result = result + val[1]
            else:
                carry = 0
                result = result + str(val)
            p1 -= 1
    
        while p2 >= 0:
            val = carry + int(num2[p2])
            if val > 9:
                val = str(val)
                carry = int(val[0])
                result = result + val[1]
            else:
                carry = 0
                result = result + str(val)
            p2 -= 1
        
        if carry > 0: result = result + str(carry)

        return result[::-1]
