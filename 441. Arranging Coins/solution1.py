class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 0
        for i in range(1 ,n + 1):
            if n - i >= 0:
                n -= i
                counter += 1
        return counter