class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(31):
            if n % 2 == 1:
                ret += 1
            ret = ret << 1
            n = n >> 1
        
        return ret + n