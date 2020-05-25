class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pos1 = 1
        pos2 = 1
        carry = 0
        ret = ''
        while pos1 <= len(a) or pos2 <= len(b):
            if pos1 > len(a):
                digit1 = 0
            else:
                digit1 = int(a[-1*pos1])
            
            if pos2 > len(b):
                digit2 = 0
            else:
                digit2 = int(b[-1*pos2])    
                
                
            if digit1 + digit2 + carry == 3:
                carry = 1
                ret = '1' + ret
            elif digit1 + digit2 + carry == 2:
                carry = 1
                ret = '0' + ret
            elif digit1 + digit2 + carry == 1:
                carry = 0
                ret = '1' + ret
            else:
                carry = 0
                ret = '0' + ret
            
            pos1 += 1
            pos2 += 1
        
        if carry == 1:
            return '1' + ret
        else:
            return ret