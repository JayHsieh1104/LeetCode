class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            if n >= 2 ** i:
                n -= 2 ** i
                ret += 2 ** (31 - i)
        return ret