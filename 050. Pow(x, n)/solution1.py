class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            for i in range(abs(n)):
                ans = ans / x
        else:
            for i in range(n):
                ans = ans * x
        return ans