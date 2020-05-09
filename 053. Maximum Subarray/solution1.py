class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pointer = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if pointer > 0:
                pointer += nums[i]
            else:
                pointer = nums[i]
            res = max(res, pointer)
        return res