class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    if dp[i - coin] + 1 < dp[i]:
                        dp[i] = dp[i - coin] + 1
        
        if dp[amount] == MAX:
            return -1
        else:
            return dp[amount]