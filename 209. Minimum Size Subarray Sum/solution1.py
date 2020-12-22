class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = len(nums)
        subarray_sum = 0
        i = 0
        for j in range(len(nums)):
            subarray_sum += nums[j]
            while subarray_sum >= s:
                subarray_sum -= nums[i]
                min_length = min(min_length, j - i + 1)
                i += 1
        
        if i == 0:
            return 0
        else:
            return min_length