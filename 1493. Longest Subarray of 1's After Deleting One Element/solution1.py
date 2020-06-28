class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # dp[i] is the length of subarray of 1's to position i.
        dp = [0] * len(nums)
        if nums[0] == 1:
            dp[0] = 1
            
        # Build DP array
        for i in range(1, len(nums)):
            if nums[i] == 1:
                dp[i] = dp[i-1] + 1
        
        # Find the longest subarray of 1's when removing nums[i]
        currentLength = dp[0]
        maxLength = currentLength
        for i in range(1, len(nums)):
            if nums[i] == 0:
                currentLength = dp[i-1]
                if currentLength > maxLength:
                    maxLength = currentLength
                for j in range(i+1, len(nums)):
                    if nums[j] == 0:
                        break
                    else:
                        if currentLength + dp[j] > maxLength:
                            maxLength = currentLength + dp[j]
        
        for i in range(len(nums)-1, -1, -1):
            if dp[i] - 1 > maxLength:
                maxLength = dp[i] - 1
        
        return maxLength