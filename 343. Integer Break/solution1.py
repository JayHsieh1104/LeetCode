class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, i):
                if j > i//2:
                    break
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j], dp[j]*dp[i-j])
        return dp[n]