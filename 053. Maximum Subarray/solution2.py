class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        max_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < dp + nums[i]:
                dp += nums[i]
            else:
                dp = nums[i]
            if dp > max_num:
                max_num = dp
        return max_num
