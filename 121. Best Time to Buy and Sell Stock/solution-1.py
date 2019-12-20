class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                if prices[i] - buy_price > max_profit:
                    max_profit = prices[i] - buy_price
        return max_profit