class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        DP = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            DP[i] = max(DP[i - 1], prices[i] - min_price)
            if min_price > prices[i]:
                min_price = prices[i]
        return DP[-1]