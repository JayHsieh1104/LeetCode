class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        largestSubsetPos = 0
        largestSubsetLen = 0
        for i in range(len(dp)):
            if dp[i] > largestSubsetLen:
                largestSubsetLen += 1
                largestSubsetPos = i
        
        ret = []
        for i in range(largestSubsetLen):
            ret.append(nums[largestSubsetPos])
            largestSubsetPos = prev[largestSubsetPos]
        
        return ret