class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                elif dp[i] + 1 < dp[i+j]:
                    dp[i+j] = dp[i] + 1
                
        return dp[len(nums) - 1]