class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]
        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]