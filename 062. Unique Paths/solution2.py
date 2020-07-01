class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for x in range(1, m):
            for y in range(1, n):
                dp[y] = dp[y-1] + dp[y]
        return dp[-1]