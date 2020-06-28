class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Return len(nums) - 1 when all of the numbers in nums are all 1
        if nums.count(1) == n:
            return n - 1
        
        dp = [[0] * n for _ in range(2)]
        if nums[0] == 1:
            dp[0][0] = 1
            dp[1][0] = 1
        
        for i in range(1, n):
            if nums[i] == 1:
                dp[0][i] = dp[0][i-1] + 1
                dp[1][i] = dp[1][i-1] + 1
            else:
                dp[0][i] = 0
                dp[1][i] = dp[0][i-1]
        
        return max(dp[1])