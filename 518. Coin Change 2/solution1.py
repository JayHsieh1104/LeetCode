class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1
        
        for j in range(1, len(dp[0])):
            dp[0][j] = 0
        
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = 0
                for k in range(len(dp[0])):
                    if j - k*coins[i-1] < 0:
                        break
                    dp[i][j] += dp[i-1][j - k*coins[i-1]]
        
        return dp[-1][-1]