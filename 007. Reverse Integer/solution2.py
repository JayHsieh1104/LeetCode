class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ret = int(str(x)[::-1])
        else:
            ret = -1*int(str(-1*x)[::-1])
        
        if ret not in range(-2**31, 2**31-1):
            return 0
        else:
            return ret