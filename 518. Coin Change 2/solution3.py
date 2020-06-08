class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(len(dp)):
                if j - coins[i-1] >= 0:
                    dp[j] += dp[j - coins[i-1]]
        
        return dp[-1]