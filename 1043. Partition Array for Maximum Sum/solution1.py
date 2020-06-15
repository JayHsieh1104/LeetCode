class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A)+1)
        for i in range(1, len(dp)):
            curMax = 0
            for k in range(1, K+1):
                if i - k < 0:
                    break
                curMax = max(curMax, A[i-k])
                dp[i] = max(dp[i], dp[i-k] + curMax * k)
        return dp[-1]