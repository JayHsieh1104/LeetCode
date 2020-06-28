class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Return len(nums) - 1 when all of the numbers in nums are all 1
        if nums.count(1) == n:
            return n - 1
        
        dp = [0] * 2
        if nums[0] == 1:
            dp[0] = dp[1] = 1
        
        maxLength = dp[1]
        for i in range(1, n):
            if nums[i] == 1:
                dp[0], dp[1] = dp[0] + 1, dp[1] + 1
            else:
                dp[0], dp[1] = 0, dp[0]
            if dp[1] > maxLength:
                maxLength = dp[1]
        
        return maxLength