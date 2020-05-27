class Solution:
    def numTrees(self, n: int) -> int:
        self.dp = {0: 1}
        for i in range(1, n+1):
            self.dp[i] = 0
            for j in range(i):
                self.dp[i] += self.dp[j] * self.dp[i-j-1]
        
        return self.dp[n]