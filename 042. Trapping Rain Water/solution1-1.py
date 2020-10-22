class Solution:
    def trap(self, height: List[int]) -> int:
        # corner case
        if len(height) < 2:
            return 0

        dp = [height[0]]
        res = 0
        for i in range(1, len(height)):
            dp.append(max(height[i], dp[i - 1]))
        dp[-1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            dp[i] = min(max(height[i], dp[i + 1]), dp[i])
        for i in range(len(height)):
            res += dp[i] - height[i]
        return res