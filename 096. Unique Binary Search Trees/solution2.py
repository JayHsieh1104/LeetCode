class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for level in range(1, n+1):
            for leftNodeNum in range(level):
                dp[level] += dp[leftNodeNum] * dp[level-1-leftNodeNum]
        return dp[n]