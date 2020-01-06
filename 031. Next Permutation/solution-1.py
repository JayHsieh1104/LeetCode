class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # For case that all numbers sorted in descending order
        if i == -1:
            nums.sort()
            return
        
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = reversed(nums[i+1:])
                return
            else:
                j -= 1