class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            if min_price > prices[i]:
                min_price = prices[i]
        return max_profit