class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            for i in range(len(num1)-len(num2)):
                num2 = '0' + num2
        else:
            for i in range(len(num2)-len(num1)):
                num1 = '0' + num1
        
        ret = ''
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            n1 = ord(num1[i]) - ord('0')
            n2 = ord(num2[i]) - ord('0')
            carry, n3 = divmod((carry + n1 + n2), 10)
            ret = str(n3) + ret
        if carry == 1:
            ret = '1' + ret
                
        return ret