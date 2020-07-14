class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        
        nums.sort()
        max_diff = float('inf')
        for i, j in [(0, -4), (1, -3), (2, -2), (3, -1)]:
            if nums[j] - nums[i] < max_diff:
                max_diff = nums[j] - nums[i]
        
        return max_diff