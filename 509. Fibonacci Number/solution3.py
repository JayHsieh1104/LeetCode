class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        else:
            self.cache = {0: 0, 1: 1}
            return self.memoize(N)
    
    def memoize(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        else:
            self.cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
            return self.cache[N]