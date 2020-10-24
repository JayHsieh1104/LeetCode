class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_interval = 0
        if len(prices) < 2:
            return max_interval
        
        min_num = prices[0]
        for i in range(1, len(prices)):
            if min_num > prices[i]:
                min_num = prices[i]
            elif min_num < prices[i] and (prices[i] - min_num) > max_interval:
                max_interval = prices[i] - min_num
        
        return max_interval