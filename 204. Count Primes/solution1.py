class Solution:
    def countPrimes(self, n: int) -> int:
        counter = 0
        isPrime = [True] * (n+1)
        for i in range(2, n):
            if isPrime[i]:
                counter += 1
                for j in range(1, (n // i)+1):
                    isPrime[i * j] = False
                    
        return counter