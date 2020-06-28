class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        
        for square in squares:
            dp[square] = 1
        
        for i in range(2, n+1):
            for square in squares:
                if i < square:
                    break
                if dp[square] + dp[i-square] < dp[i]:
                    dp[i] = dp[square] + dp[i-square]
        
        return dp[n]