class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * (mid + 1) / 2 <= n:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1