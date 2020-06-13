class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cur = 1
        while cur <= n:
            if cur == n:
                return True
            cur *= 2
        return False