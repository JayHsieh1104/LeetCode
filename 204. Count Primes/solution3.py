class Solution:
    def countPrimes(self, n: int) -> int:
        counter = 0
        isPrime = [True] * (n+1)
        for i in range(2, int(math.sqrt(n))+1):
            if isPrime[i]:
                for j in range(i, (n // i)+1):
                    isPrime[i * j] = False
                    
        for i in range(2, n):
            if isPrime[i]:
                counter += 1
                    
        return counter