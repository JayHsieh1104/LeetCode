class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        i = 0
        j = 1

        while i < len(nums) and j < len(nums):
            if nums[j] - nums[i] < k or i == j:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                i += 1
                result += 1
                while i < len(nums) and nums[i-1] == nums[i]:
                    i += 1

        return result
