class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 1:
                return abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1