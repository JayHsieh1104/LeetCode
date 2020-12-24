class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            max_so_far = min_so_far = 1
            result = nums[0]
            for num in nums:
                max_so_far, min_so_far = max(
                    num, num * max_so_far, num * min_so_far), min(num, num * max_so_far, num * min_so_far)
                result = max(result, max_so_far)

            return result
