class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(arr[i:k + 1]) * max(arr[k + 1:j + 1]) + dp[i][k] + dp[k + 1][j])

        return dp[0][n - 1]
