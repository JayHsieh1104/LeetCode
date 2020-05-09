class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:  # corner case
            return 0
        
        maxSum = 0
        minNum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxSum = max(maxSum, prices[i] - minNum)
            if prices[i] < minNum:
                minNum = prices[i]
        return maxSum