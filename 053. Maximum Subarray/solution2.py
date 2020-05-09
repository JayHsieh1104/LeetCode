class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        res = dp
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            if dp > res:
                res = dp
        return res