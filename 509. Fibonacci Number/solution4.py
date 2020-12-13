class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        else:
            prev1 = 0
            prev2 = 1
            for i in range(2, N + 1):
                prev1, prev2 = prev2, prev1 + prev2
        
        return prev2
